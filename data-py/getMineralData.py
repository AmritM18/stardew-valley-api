import requests
from bs4 import BeautifulSoup
import pandas as pd

def getMineralData(mineralIndices):
    mineralSite = "https://stardewvalleywiki.com/Minerals"
    req = requests.get(mineralSite).text
    req = req.split("id=\"Foraged_Minerals\"")
    req = req[1]
    req = req.split("id=\"Geodes\"")
    geodeReq = req[1]
    req = req[0]
    soup = BeautifulSoup(req,'lxml')

    table = soup.find_all('table',{'class':'wikitable'})
    mineralRows = []
    
    # looking at all of the tables except for the last 3 (geodes, collection, history)
    for i in range(0, len(table)):
        rows = table[i].findChildren('tr', recursive=False)
        for i in range(1, len(rows)):
            tds = rows[i].findChildren('td', recursive=False)

            mineral = [tds[x].text.strip(' ').strip('\n').replace('\xa0', '') for x in mineralIndices]

            # extra formatting
            locations = tds[4].findChildren(recursive=False)
            locationtd = []
            for location in locations:
                locationtd.append(location.text)
            locationtd = ', '.join(locationtd)
            mineral[2] = locationtd.strip(' ').strip('\n').replace('\xa0', '').replace(', monster, the mines', '')

            uses = tds[5].findChildren(recursive=False)
            usesTd = []
            for use in uses:
                usesTd.append(use.text)
            usesTd = ', '.join(usesTd)
            mineral[3] = usesTd.strip(' ').strip('\n').replace('\xa0', '')

            mineralRows.append(mineral)

    # process geode table
    geodeSoup = BeautifulSoup(geodeReq,'lxml')
    table = geodeSoup.find('table',{'class':'wikitable'})
    rows = table.findChildren('tr', recursive=False)
    for i in range(1, len(rows)):
        tds = rows[i].findChildren('td', recursive=False)
        
        geodeIndices = [1,2,3,4]
        
        geode = [tds[x].text.strip(' ').strip('\n').replace('\xa0', '') for x in geodeIndices]

        # extra formatting
        geode[1] = ''

        parentList = tds[3].findChildren()
        locations = parentList[0].findChildren(recursive=False)
        locationtd = []
        for location in locations:
            locationtd.append(location.text)
        locationtd = ', '.join(locationtd)
        geode[2] = locationtd.strip().replace('\xa0', '')

        uses = tds[4].findChildren(recursive=False)
        usesTd = []
        for use in uses:
            usesTd.append(use.text)
        usesTd = ', '.join(usesTd)
        geode[3] = usesTd.strip(' ').strip('\n').strip(',').strip().replace('\xa0', '')

        mineralRows.append(geode)

    return mineralRows

def main():
    # Go to Minerals page and choose the columns you want
    mineralColumns = ["Name", "Sell", "Location", "Uses"]
    mineralIndices = [1,3,4,5]

    df = pd.DataFrame(columns=mineralColumns)
    mineralRows = getMineralData(mineralIndices)
    for item in mineralRows:
        df = df.append(pd.Series(item, index=mineralColumns), ignore_index=True)


    df.to_csv("/home/amrit/projects/MineralData.csv", index=False, encoding='utf-8')

if __name__ == "__main__":
    main()