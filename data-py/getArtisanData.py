import requests
from bs4 import BeautifulSoup
import pandas as pd

def getBeeHouseData(req, indices):
    clip = req.split("id=\"Bee_House\"")
    clip = clip[1]
    soup = BeautifulSoup(clip,'lxml')
    table = soup.findAll('table',{'class':'wikitable'})
    
    # looking at all of the tables except for the last 3 (geodes, collection, history)
    rows = table[1].findChildren('tr', recursive=False)
    tds = tds = rows[1].findChildren('td', recursive=False)
    honey = [tds[x].text.strip(' ').strip('\n').replace('\xa0', '') for x in indices]
    honey[3] = honey[3] + ': ' + tds[7].text.strip().replace('\xa0', '')
    honey.append('Bee House')
    for i in range(2, len(rows)):
        tds = rows[i].findChildren('td', recursive=False)
        if len(tds) == 3: honey[3] = honey[3] + ', ' + tds[1].text.strip() + ': ' + tds[2].text.strip()
        elif len(tds) == 2: honey[3] = honey[3] + ', ' + tds[0].text.strip() + ': ' + tds[1].text.strip()
    return honey

def getCaskData(req, indices):
    clip = req.split("id=\"Cask\"")
    clip = clip[1]
    soup = BeautifulSoup(clip,'lxml')
    table = soup.findAll('table',{'class':'wikitable'})
    caskData = []

    rows = table[1].findChildren('tr', recursive=False)
    for i in range(1, len(rows)):
        tds = rows[i].findChildren('td', recursive=False)

        cask = [tds[x].text.strip().replace('\xa0', '') for x in indices] # only gives us name and recipe

        # now process the Time and Sell tds[3] -- tds[6]
        cask.append('0 Days')
        cask.append(tds[3].text.strip())

        cask[2] = cask[2] + ', ' + tds[4].text[(tds[4].text.rfind(':'))+2:].strip() + ' (Silver)'
        cask[3] = cask[3] + ', ' + tds[4].text[:tds[4].text.rfind('Aged')].strip() + ' (Silver)'

        cask[2] = cask[2] + ', ' + tds[5].text[(tds[5].text.rfind(':'))+2:].strip() + ' (Gold)'
        cask[3] = cask[3] + ', ' + tds[5].text[:tds[5].text.rfind('Aged')].strip() + ' (Gold)'

        cask[2] = cask[2] + ', ' + tds[6].text[(tds[6].text.rfind(':'))+2:].strip() + ' (Iridium)'
        cask[3] = cask[3] + ', ' + tds[6].text[:tds[6].text.rfind('Aged')].strip() + ' (Iridium)'

        cask.append('Cask')
        caskData.append(cask)
    return caskData

# This requires the oil to have only 2 rows 
def getOilMakerData(req, indices):
    clip = req.split("id=\"Oil_Maker\"")
    clip = clip[1]
    soup = BeautifulSoup(clip,'lxml')
    table = soup.findAll('table',{'class':'wikitable'})
    data = []

    rows = table[1].findChildren('tr', recursive=False)
    tds = rows[1].findChildren('td', recursive=False)
    oil = [tds[x].text.strip().replace('\xa0', '') for x in indices]
    oil.append('Oiler Maker')
    data.append(oil)

    tds = rows[2].findChildren('td', recursive=False)
    oil = [tds[x].text.strip().replace('\xa0', '') for x in indices]
    oil.append('Oiler Maker')

    for i in range(3, 5):
        tds = rows[i].findChildren('td', recursive=False)
        oil[1] = oil[1] + ', ' + tds[0].text.strip()
        oil[2] = oil[2] + ', ' + tds[1].text.strip()

    data.append(oil)

    return data

def getArtisanData(name, req, indices):
    clip = req.split("id=\"" + name.replace(' ', '_') + "\"")
    clip = clip[1]
    soup = BeautifulSoup(clip,'lxml')
    table = soup.findAll('table',{'class':'wikitable'})
    data = []

    rows = table[1].findChildren('tr', recursive=False)
    for i in range(1, len(rows)):
        tds = rows[i].findChildren('td', recursive=False)

        item = [tds[x].text.strip().replace('\xa0', '') for x in indices]
        item.append(name)

        if name == "Mayonnaise Machine" or name == "Cheese Press":
            item[3] = item[3].replace(' ', '').replace('\n', '').replace('g', 'g, ', 1)

        data.append(item)
    return data

def main():
    # Artisan goods found here: https://stardewvalleywiki.com/Artisan_Goods
    # By default, each category has 5 columns unless otherwise stated
        # Bee House
        # Cask
        # Cheese Press
        # Keg
        # Loom
        # Mayonnaise Machine
        # Oil Maker
        # Preserves Jar
    site = "https://stardewvalleywiki.com/Artisan_Goods"
    req = requests.get(site).text
    columns = ['Name', 'Recipe', 'Time', 'Sell', 'Equipment']
    indices = [1, 3, 4, 5]
    df = pd.DataFrame(columns=columns)

    # Honey
    beeHouseIndices = [1, 2, 4, 6]
    honey = getBeeHouseData(req, beeHouseIndices)
    df = df.append(pd.Series(honey, index=columns), ignore_index=True)
    
    # Cask Data
    caskIndices = [1, 2]     # time and sell need to be determined from columns 3,4,5,6
    caskData = getCaskData(req, caskIndices)
    for item in caskData:
        df = df.append(pd.Series(item, index=columns), ignore_index=True)

    # Cheese Press
    name = "Cheese Press"
    pressData = getArtisanData(name, req, indices)
    for item in pressData:
        df = df.append(pd.Series(item, index=columns), ignore_index=True)
    
    # Keg
    name = "Keg"
    kegData = getArtisanData(name, req, indices)
    for item in kegData:
        df = df.append(pd.Series(item, index=columns), ignore_index=True)
    
    # Loom
    name = "Loom"
    loomData = getArtisanData(name, req, indices)
    for item in loomData:
        df = df.append(pd.Series(item, index=columns), ignore_index=True)
    
    # Mayonnaise Machine
    name = "Mayonnaise Machine"
    mayonnaiseMachineData = getArtisanData(name, req, indices)
    for item in mayonnaiseMachineData:
        df = df.append(pd.Series(item, index=columns), ignore_index=True)

    # Oil Maker
    oilMakerData = getOilMakerData(req, indices)
    for item in oilMakerData:
        df = df.append(pd.Series(item, index=columns), ignore_index=True)

    # Preserves Jar
    name = "Preserves Jar"
    preservesJarData = getArtisanData(name, req, indices)
    for item in preservesJarData:
        df = df.append(pd.Series(item, index=columns), ignore_index=True)
    
    df.to_csv("/home/amrit/projects/ArtisanData.csv", index=False, encoding='utf-8')

if __name__ == "__main__":
    main()