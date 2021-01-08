import requests
from bs4 import BeautifulSoup
import pandas as pd

def getVillagerData():
    gift_site = "https://stardewvalleywiki.com/List_of_All_Gifts"
    req = requests.get(gift_site).text
    soup = BeautifulSoup(req,'lxml')

    table = soup.find('table',{'class':'wikitable sortable'})
    rows = table.find_all('tr')
    #columns = [v.text.replace('\n', '').replace('\xa0', '').replace(' ', '').replace('(+80)', '').replace('(+45)','').replace('(-20)','').replace('(+20)','').replace('(-40)','')
    #                for v in rows[0].find_all('th')]
    villagerRows = []
    for i in range(2, len(rows)):
        tds = rows[i].find_all('td')

        villager = [tds[0].text.replace(' ', '').replace('\n',''),  # Villager
                        tds[1].text.strip('\n'), # Birthday
                        tds[2].text.strip('\n').replace('\n',',').strip(' '), # Loves
                        tds[3].text.strip('\n').replace('\n', ',').strip(' '), # Likes
                        tds[4].text.strip('\n').replace('\n', ',').strip(' '), # Neutral
                        tds[5].text.strip('\n').replace('\n', ',').strip(' '), # Dislikes
                        tds[6].text.strip('\n').replace('\n', ',').strip(' ')] # Hates

        #print(villager)
        #df = df.append(pd.Series(villager, index=columns), ignore_index=True)
        villagerRows.append(villager)
        
    #print(df)
    #df.to_csv('/home/amrit/projects/VillagerData.csv', index=False, encoding='utf-8')
    return villagerRows

def main():
    # Go to List of Gifts page and choose the columns you want
    villagerColumns = ["Villager", "Birthday", "Loves", "Likes", "Neutral", "Dislikes", "Hates"]
    df = pd.DataFrame(columns=villagerColumns)
    villagerRows = getVillagerData()
    for item in villagerRows:
        df = df.append(pd.Series(item, index=villagerColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/VillagerData.csv", index=False, encoding='utf-8')

if __name__ == "__main__":
    main()