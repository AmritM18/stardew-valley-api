import requests
from bs4 import BeautifulSoup
import pandas as pd

# Info taken from https://stardewvalleywiki.com/Animals
# We look at all tables with 5 or 6 columns
def getFoodProductData(name, req, fiveIndices, sixIndices):
    clip = req.split("id=\"" + name.replace(' ', '_') + "\"")
    clip = clip[1]
    soup = BeautifulSoup(clip,'lxml')
    table = soup.find('table',{'class':'wikitable'})
    data = []
    lastAnimalEntry = ''

    rows = table.findChildren('tr', recursive=False)

    for i in range(1, len(rows)):
        tds = rows[i].findChildren('td', recursive=False)
        if tds[1].text.strip() != lastAnimalEntry:
            if len(tds) == 5:
                #print(tds[1].text.strip())
                #print(len(tds))
                rowNumbers = tds[3].text.count('-')
                produces = tds[3].text.strip()
                for j in range(0, rowNumbers):
                    productName = produces.split(' - ', 1)[0]
                    produces = produces.split(' - ', 1)[1]
                    sell = produces.split(' ', 1)[0]
                    sell = sell + ', ' + str(int(float(sell.strip('g'))*1.25)) + 'g, ' + str(int(float(sell.strip('g'))*1.5)) + 'g, ' + str(int(float(sell.strip('g'))*2)) + 'g'
                    if len(produces.split('g ', 1)) > 1:
                        produces = produces.split('g ', 1)[1]
                    product = [tds[x].text.replace('\xa0', '').strip() for x in fiveIndices]
                    product = [productName.strip()] + [sell.strip()] + product
                    product.append('')
                    data.append(product)
                lastAnimalEntry = tds[1].text.strip()
            elif len(tds) == 6:
                rowNumbers = tds[4].text.count('-')
                produces = tds[4].text.strip()
                for j in range(0, rowNumbers):
                    productName = produces.split(' - ', 1)[0]
                    produces = produces.split(' - ', 1)[1]
                    sell = produces.split(' ', 1)[0]
                    sell = sell + ', ' + str(int(float(sell.strip('g'))*1.25)) + 'g, ' + str(int(float(sell.strip('g'))*1.5)) + 'g, ' + str(int(float(sell.strip('g'))*2)) + 'g'
                    if len(produces.split('g ', 1)) > 1:
                        produces = produces.split('g ', 1)[1]
                    product = [tds[x].text.replace('\xa0', '').strip() for x in sixIndices]
                    product = [productName.strip()] + [sell.strip()] + product
                    data.append(product)
                lastAnimalEntry = tds[1].text.strip()
    return data

def main():
    site = "https://stardewvalleywiki.com/Animals"
    req = requests.get(site).text
    columns = ['Name', 'Sell', 'Animal', 'Cost', 'Requirement']
    animals = ['Chickens', 'Ducks', 'Rabbits', 'Dinosaurs', 'Cows', 'Goats', 'Sheep', 'Pigs']
    fiveColumnIndex = [1,2]
    sixColumnIndex = [1,2,3]   # 3 is where the requirements is AND we determine cost and sell in the code
    df = pd.DataFrame(columns=columns)

    for animal in animals:
        foodProductRows = getFoodProductData(animal, req, fiveColumnIndex, sixColumnIndex)
        for product in foodProductRows:
            df = df.append(pd.Series(product, index=columns), ignore_index=True)
    df.to_csv("/home/amrit/projects/AnimalProductData.csv", index=False, encoding='utf-8')

if __name__ == "__main__":
    main()