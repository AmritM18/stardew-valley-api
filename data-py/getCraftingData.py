import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def getCraftingData(name, req, fiveColumnsIndices):
    clip = req.split("id=\"" + name + "\"")
    clip = clip[1]
    soup = BeautifulSoup(clip,'lxml')
    table = soup.find('table',{'class':'wikitable'})
    finalRows = []
    
    # looking at all of the tables except for the last 3 (geodes, collection, history)

    rows = table.findChildren('tr', recursive=False)
    for i in range(1, len(rows)):
        tds = rows[i].findChildren('td', recursive=False)
        
        item = [tds[x].text.strip(' ').strip('\n').replace('\xa0', '') for x in fiveColumnsIndices]
        
        # extra formatting
        item[0] = item[0].replace(':', '')
        item[0] = re.sub(r" \(\d+\)", "", item[0])
        item[2] = item[2].replace(')', '),', item[2].count(')')-1)
        if '(Sp)(Spring Seeds)' in item[0]:
            item[0] = item[0][:item[0].find('(', 1)-1]
            item[0] = item[0] + " Summer"
        elif "(Su)(Summer Seeds)" in item[0]:
            item[0] = item[0][:item[0].find('(', 1)-1]
            item[0] = item[0] + " Spring"
        elif "(Fa)(Fall Seeds)" in item[0]:
            item[0] = item[0][:item[0].find('(', 1)-1]
            item[0] = item[0] + " Fall"
        elif "(Wi)(Winter Seeds)" in item[0]:
            item[0] = item[0][:item[0].find('(', 1)-1]
            item[0] = item[0] + " Winter"
        elif "(Fe)" in item[0]:
            item[0] = item[0][:item[0].find('(', 1)-1]
            item[0] = item[0] + " Iron"
        elif "(Au)" in item[0]:
            item[0] = item[0][:item[0].find('(', 1)-1]
            item[0] = item[0] + " Gold"
        else: 
            if item[0].find('(', 1) > 0:
                item[0] = item[0][:item[0].find('(', 1)-1]
        
        finalRows.append(item)
    return finalRows


def main():
    # Supported categories for crafting found here: https://stardewcommunitywiki.com/Crafting
    # By default, each category has 5 columns unless otherwise stated
        # Bombs   (7)
        # Fences   (6)
        # Edible   (7 COLUMNS)
        # Sprinklers  (5)
        # Artisan Equipment  (5)
        # Fertilizer  (5)
        # Seeds (5)
        # Decor (5)
        # Fishing  (5)
        # Rings (5)
        # Consumables (5)
        # Lighting (5)
        # Refining Equipment (5)
        # Furniture (5)
        # Misc (5)
    
    fiveColumns = ["Name", "Description", "Recipe", "Source"]
    fiveColumnsIndices = [1,2,3,4]
    site = "https://stardewvalleywiki.com/Crafting"
    req = requests.get(site).text

    edibleColumns = ["Name", "Description", "Recipe", "Energy", "Health", "Source"]
    edibleIndices = [1,2,3,4,5,6]
    name = "Edible_Items"
    df = pd.DataFrame(columns=edibleColumns)
    edibleRows = getCraftingData(name, req, edibleIndices)
    for item in edibleRows:
        df = df.append(pd.Series(item, index=edibleColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_Edible.csv", index=False, encoding='utf-8')

    bombColumns = ["Name", "Description", "Recipe", "Radius", "Source", "Sell"]
    bombIndices = [1,2,3,4,5,6]
    name = "Bombs"
    df = pd.DataFrame(columns=bombColumns)
    bombRows = getCraftingData(name, req, bombIndices)
    for item in bombRows:
        df = df.append(pd.Series(item, index=bombColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_Bombs.csv", index=False, encoding='utf-8')

    fenceColumns = ["Name", "Description", "Life", "Recipe", "Source"]
    fenceIndices = [1,2,3,4,5]
    name = "Fences"
    df = pd.DataFrame(columns=fenceColumns)
    fenceRows = getCraftingData(name, req, fenceIndices)
    for item in fenceRows:
        df = df.append(pd.Series(item, index=fenceColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_Fences.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Sprinklers"
    sprinklersRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in sprinklersRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_SprinklerData.csv", index=False, encoding='utf-8')
    
    df = pd.DataFrame(columns=fiveColumns)
    name = "Artisan_Equipment"
    artisanEquipmentRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in artisanEquipmentRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_ArtisanEquipmentData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Fertilizer"
    fertilizerRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in fertilizerRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_FertilizerData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Seeds"
    seedRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in seedRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_SeedData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Decor"
    decorRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in decorRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_DecorData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Fishing"
    fishingRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in fishingRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_FishingData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Rings"
    ringRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in ringRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_RingsData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Consumables"
    consumableRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in consumableRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_ConsumableData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Lighting"
    lightingRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in lightingRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_LightingData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Refining_Equipment"
    equipmentRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in equipmentRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_RefiningEquipmentData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Furniture"
    furnitureRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in furnitureRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_FurnitureData.csv", index=False, encoding='utf-8')

    df = pd.DataFrame(columns=fiveColumns)
    name = "Misc"
    miscRows = getCraftingData(name, req, fiveColumnsIndices)
    for item in miscRows:
        df = df.append(pd.Series(item, index=fiveColumns), ignore_index=True)
    df.to_csv("/home/amrit/projects/Crafting_MiscData.csv", index=False, encoding='utf-8')    
    

if __name__ == "__main__":
    main()