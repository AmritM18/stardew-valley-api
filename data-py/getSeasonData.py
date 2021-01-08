# In our Season model, we want 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def trimStart(cropRows):
    while (cropRows[0].find('days') == -1):
        cropRows.pop(0)
    return cropRows

def getPricesAndTrimEnd(cropRows):
    for i in range(1, len(cropRows)):
        if re.search(r'([0-9,]+g)+', cropRows[i]):
            return cropRows[:i+1]

def popXP(cropRows):
    index = -1
    for i in range(1, len(cropRows)):
        if (cropRows[i].find('XP') != -1):
            index = i
            break
    if (index != -1): cropRows.pop(index)
    return cropRows

def combineHealthEnergy(cropRows):
    index = -1
    for i in range(1, len(cropRows)):
        if 'Energy' in cropRows[i]:
            index = i
            break
    if index != -1 and 'Health' in cropRows[index+1]: 
        cropRows[index:index+2] = [' '.join(cropRows[index:index+2])]
    return cropRows

def digestRows(seasonRows, season):
    finalCrop = []
    for i in range(1, len(seasonRows)):
        tds = seasonRows[i].find_all('td')

        cropSite = "https://stardewvalleywiki.com/"
        cropSite += (tds[0].text.strip(' ').replace(' ', '_'))
        cropWiki = requests.get(cropSite).text
        cropSoup = BeautifulSoup(cropWiki,'lxml')

        cropTable = cropSoup.find('table',{'id':'infoboxtable'})

        cropRows = [v.text.replace('\n', '').replace('\xa0', '').strip(' ').replace(' • ', ' & ')
                    for v in cropTable.findAll('td', {'id':'infoboxdetail'})]

        cropRows = trimStart(cropRows)
        cropRows = popXP(cropRows)
        cropRows = combineHealthEnergy(cropRows)
        cropRows = getPricesAndTrimEnd(cropRows)

        for j in range (1, len(cropRows)):
            cropRows[j] = " ".join(cropRows[j].split())

        cropRows[1] = season

        crop = [tds[0].text.strip(' ').replace('\n',''),
                tds[1].text.strip('\n').strip(' ')]
        crop = crop + cropRows

        finalCrop.append(crop)
    return finalCrop

def getSeasonDataCrops():
    # Not doing winter since it doesn't have any crops
    cropSeasons = ["Spring", "Summer", "Fall"]
    #sCol = ["Crop", "Seed Price", "Growth Time", "Season", "Healing", "Sell Prices"] # find a better soln for this
    #df = pd.DataFrame(columns=sCol)
    cropRows = []

    for item in cropSeasons:
        seasonSite = "https://stardewvalleywiki.com/" + item
        seasonWiki = requests.get(seasonSite).text
        seasonWiki = seasonWiki.split("id=\"Crops\"")
        seasonWiki = seasonWiki[1]
        seasonWiki = seasonWiki.split("id=\"Forage\"")
        seasonWiki = seasonWiki[0]
        seasonSoup = BeautifulSoup(seasonWiki,'lxml')

        seasonTable = seasonSoup.findAll('table',{'class':'wikitable'})
        for table in seasonTable:    
            seasonRows = table.find_all('tr')
            print(seasonRows[0].find('th'))
            #seasonColumns = [v.text.replace('\n', '').replace('\xa0', '').replace(' ', '')
            #                for v in seasonRows[0].find_all('th')]
            #if seasonColumns[0] != "Crop": continue
            #seasonColumns = seasonColumns[:2]

            # digest rows can be sped up
            crops = digestRows(seasonRows, item)
            for x in crops:
                cropRows.append(x)
    return cropRows
    #df.to_csv("/home/amrit/projects/CropData.csv", index=False, encoding='utf-8')

def getSeasonDataForage():
    forageSeasons = ["Spring", "Summer", "Fall", "Winter"]
    # Go to Spring/Summer/Winter/Fall and choose rows if they've changed
    # indices           2        4          5            7
    #forageColumns = ["Forage", "Season", "Location", "Sell", "Uses"]
    #df = pd.DataFrame(columns=forageColumns)
    forageRows = []

    for item in forageSeasons:
        seasonSite = "https://stardewvalleywiki.com/" + item
        seasonWiki = requests.get(seasonSite).text
        seasonWiki = seasonWiki.split("id=\"Forage\"")
        seasonWiki = seasonWiki[1]
        seasonWiki = seasonWiki.split("id=\"Fish\"")
        seasonWiki = seasonWiki[0]
        seasonSoup = BeautifulSoup(seasonWiki,'lxml')
        seasonTable = seasonSoup.findAll('table',{'class':'wikitable'})
        for table in seasonTable:    
            seasonRows = table.find_all('tr')
            i = 1
            while i < len(seasonRows):
                tds = seasonRows[i].find_all('td')
                
                # use this to find whats in each td
                #j = 0
                #print("len tds: ", len(tds))
                #while j < len(tds):
                #    print("tds number ", j)
                #    print(tds[j].text)
                #    j += 1

                usedInTags = tds[-1].findChildren(recursive=False)
                usedIn = []
                for tags in usedInTags:
                    usedIn.append(tags.text)
                usedIn = ",".join(usedIn)

                gCommas = tds[4].text.count('g') - 1
                
                forage = [tds[1].text.strip(' ').replace('\n',''),
                          item,
                          tds[3].text.strip('\n').replace('\n',', ').strip(' '),
                          tds[4].text.strip('\n').strip(' ').replace('\n', '').replace(' ', '').replace('g', 'g, ', gCommas),
                          usedIn.strip(' ')]
                #df = df.append(pd.Series(forage, index=forageColumns), ignore_index=True)
                forageRows.append(forage)
                
                # this skips all of the tables embedded in the table
                # I think we can do a findChildren(recursive false to avoid this)
                i += 10  
    #print(df)
    #df.to_csv("/home/amrit/projects/ForageData.csv", index=False, encoding='utf-8')
    return forageRows

def getSeasonDataFish():
    fishSeasons = ["Spring", "Summer", "Fall", "Winter"]
    # Go to Spring/Summer/Winter/Fall and choose rows if they've changed
    # indices         2       4          7         8       9          10             12      14  
    #fishColumns = ["Fish", "Season", "Sell", "Location", "Time", "Weather", "Difficulty", "Uses"]
    #df = pd.DataFrame(columns=fishColumns)
    fishRows = []

    for item in fishSeasons:
        seasonSite = "https://stardewvalleywiki.com/" + item
        seasonWiki = requests.get(seasonSite).text
        seasonWiki = seasonWiki.split("id=\"Fish\"")
        seasonWiki = seasonWiki[1]   # Fish should be the last header
        seasonSoup = BeautifulSoup(seasonWiki,'lxml')
        # Only need to find 1 table (except for winter where there's a night market)
        seasonTable = seasonSoup.find('table',{'class':'wikitable'})
        seasonRows = seasonTable.findChildren('tr', recursive=False)
        #for table in seasonTable:
        #print(seasonTable)
        #break
        #seasonRows = seasonTable.findAll('tr')
        i = 1
        while i < len(seasonRows):
            tds = seasonRows[i].find_all('td')
            
            # use this to find whats in each td
            #j = 0
            #print("len tds: ", len(tds))
            #while j < len(tds):
            #    print("tds number ", j)
            #    print(tds[j].text)
            #    j += 1

            usedInTags = tds[-1].findChildren(recursive=False)
            usedIn = []
            for tags in usedInTags:
                usedIn.append(tags.text)
            usedIn = ",".join(usedIn)

            gCommas = tds[3].text.count('g') - 1

            location = tds[30].text.strip('\n').strip(' ')
            index = 0
            while index < len(location):
                if location[index] == ')' and index < len(location)-1:
                    location = location[0:index+1] + ", " + location[index+1:]
                if location[index].isupper() and index > 0:
                    if location[index-1].islower():
                        location = location[0:index] + ", " + location[index:]
                if location[index] == ',' and index < len(location) - 1:
                    if location[index+1].isalpha():
                        location = location[0:index+1] + " " + location[index+1:]
                index += 1
            
            time = tds[31].text.strip('\n').strip(' ').replace('\n', '')
            index = 0
            while index < len(time):
                if time[index] == 'm' and index < len(time)-1:
                    if time[index+1].isdigit():
                        time = time[0:index+1] + ", " + time[index+1:]
                index += 1

            weather = tds[33].text.strip('\n').strip(' ').replace('\n', '').replace(' ', ' & ')
            while weather[0].isalpha() == 0:
                weather = weather[1:]
            index = 0
            while index < len(weather):
                if weather[index].isalpha() == 0 and weather[index-1] != ',':
                    weather = weather[0:index] + ", " + weather[index+1:]
                index += 1
            
            # want 1, 3, 30, 31, 32, 33, 35, and the last one
            fish = [tds[1].text.strip(' ').replace('\n',''), #GOOD
                        item,
                        tds[3].text.strip('\n').strip(' ').replace('\n', '').replace(' ', '').replace('g', 'g, ', gCommas), #GOOD
                        location, # GOOD
                        time,  # GOOD
                        weather, # Sun Wind Â 
                        tds[35].text.strip('\n').strip(' ').replace('\n', ''), #GOOD
                        usedIn.strip(' ')]
            fishRows.append(fish)
            i += 1
    
    return fishRows
    #print(df)
    #df.to_csv("/home/amrit/projects/FishData.csv", index=False, encoding='utf-8')

def getSeasonFruitData(df):
    fruitSite = "https://stardewvalleywiki.com/Fruits"
    fruitWiki = requests.get(fruitSite).text
    fruitSoup = BeautifulSoup(fruitWiki,'lxml')
    fruitTable = fruitSoup.find('table',{'class':'wikitable'})
    rows = fruitTable.findChildren('tr', recursive=False)
    fruitRows = []

    for i in range(1, len(rows)):
        tds = rows[i].findChildren('td', recursive=False)
        fruitName = tds[1].text.strip('\n').strip(' ').replace('\xa0', '')
        if fruitName not in df.values:
            #df['Crop'].str.contains(tds[1].text.strip('\n').strip(' ').replace('\xa0', ''), case=False):  
            #if tds[2].text.strip('\n').strip(' ').replace('\xa0', '') == "Fruit Trees": # check if it's fruit trees
            #    # check sapling site
            fruitName.replace(' ', '_')
            if tds[2].text.strip('\n').strip(' ').replace('\xa0', '') == "Fruit Trees":
                sapSite = "https://stardewvalleywiki.com/" + fruitName + "_Sapling"
                sapWiki = requests.get(sapSite).text
                sapSoup = BeautifulSoup(sapWiki,'lxml')
                sapTable = sapSoup.find('table',{'id':'infoboxtable'})

                sapRow = [v.text.replace('\n', '').replace('\xa0', '').strip(' ').replace(' • ', ' & ')
                                for v in sapTable.findAll('td', {'id':'infoboxdetail'})]
                
                fruit = [tds[1].text.strip(),   # Crop
                        sapRow[4],           # Seed Price
                        sapRow[2],           # Growth Time
                        tds[3].text.strip().replace('\xa0', ', ', (tds[3].text.count('\xa0')-1)),   # Season
                        'N/A',   # Healing
                        tds[5].text.strip().replace('\n', '')]   # Sell Price
                fruitRows.append(fruit)
            elif tds[2].text.strip('\n').strip(' ').replace('\xa0', '') == "Farming":
                cropSite = "https://stardewvalleywiki.com/" + fruitName
                cropWiki = requests.get(cropSite).text
                cropSoup = BeautifulSoup(cropWiki,'lxml')
                cropTable = cropSoup.find('table',{'id':'infoboxtable'})

                cropRow = [v.text.replace('\n', '').replace('\xa0', '').strip(' ').replace(' • ', ' & ')
                                for v in cropTable.findAll('td', {'id':'infoboxdetail'})]

                fruit = [tds[1].text.strip(),   # Crop
                        'N/A',           # Seed Price
                        cropRow[2],           # Growth Time
                        tds[3].text.strip().replace('\xa0', ', ', (tds[3].text.count('\xa0')-1)),   # Season
                        'N/A',   # Healing
                        tds[5].text.strip().replace('\n', '')]   # Sell Price
                fruitRows.append(fruit)
    return fruitRows


def main():
    # Go to Spring/Summer/Winter/Fall and choose rows if they've changed
      
    # choose these columns ahead of time and code accordingly
    forageColumns = ["Forage", "Season", "Location", "Sell", "Uses"]
    df = pd.DataFrame(columns=forageColumns)
    forageRows = getSeasonDataForage()
    for item in forageRows:
        df = df.append(pd.Series(item, index=forageColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Season_ForageData.csv", index=False, encoding='utf-8')

    # indices         2       4          7         8       9          10             12      14  
    fishColumns = ["Fish", "Season", "Sell", "Location", "Time", "Weather", "Difficulty", "Uses"]
    df = pd.DataFrame(columns=fishColumns)
    fishRows = getSeasonDataFish()
    for item in fishRows:
        df = df.append(pd.Series(item, index=fishColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Season_FishData.csv", index=False, encoding='utf-8')

    cropColumns = ["Crop", "Seed Price", "Growth Time", "Season", "Healing", "Sell Prices"] # find a better soln for this
    df = pd.DataFrame(columns=cropColumns)
    cropRows = getSeasonDataCrops()
    for item in cropRows:
        df = df.append(pd.Series(item, index=cropColumns), ignore_index=True)
    # need to get all
                    # fruits   sap          sap            fruit    fruits      fruits
    fruitRows = getSeasonFruitData(df)   # throw in the crop dataframe
    for item in fruitRows:
        df = df.append(pd.Series(item, index=cropColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Season_CropData.csv", index=False, encoding='utf-8')
   

if __name__ == "__main__":
    main()