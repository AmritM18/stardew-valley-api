import pandas as pd
import requests
from getSeasonData import getSeasonDataForage, getSeasonDataFish, getSeasonDataCrops
from getVillagerData import getVillagerData
from getRecipeData import getRecipeData
from getMineralData import getMineralData
from getCraftingData import getCraftingData
from getArtisanData import getArtisanData, getOilMakerData, getBeeHouseData, getCaskData
from getAnimalProductData import getFoodProductData

itemColumns = ['Item', 'Category']
df = pd.DataFrame(columns=itemColumns)

# get villager information (villager is first column)
villagerData = getVillagerData()
for villager in villagerData:
    item = [villager[0], 'villager']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

# get season information (season is first column)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for season in seasons:
    item = [season, 'season']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

# get crop information (crop is first column)
cropData = getSeasonDataCrops()
for crop in cropData:
    item = [crop[0], 'crop']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

# get forage information (forage is first column)
forageData = getSeasonDataForage()
for forage in forageData:
    item = [forage[0], 'forage']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

# get fish information (fish is first column)
fishData = getSeasonDataFish()
for fish in fishData:
    item = [fish[0], 'fish']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

craftingData = ['Recipe', 'Mineral', 'Edible', 'Bombs', 'Fence',
                'Sprinkler', 'Artisan Equipment', 'Fertilizer',
                'Seed', 'Decor', 'Fishing', 'Ring', 'Fence',
                'Lighting', 'Refining Equipment', 'Furniture',
                'Misc']
for category in craftingData:
    item = [category, 'crafting']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

recipeIndices = [1,3,4,5,6,7,8]
recipeData = getRecipeData(recipeIndices)
for recipe in recipeData:
    item = [recipe[0], 'recipe']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

mineralIndices = [1,3,4,5]
mineralData = getMineralData(mineralIndices)
for mineral in mineralData:
    item = [mineral[0], 'mineral']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

# Note: Crafting data uses a single function, requires the webpage to be handed
#       to it, the name of the table you want, and the indices you want.
craftingIndices = [1,2,3,4]
craftSite = "https://stardewvalleywiki.com/Crafting"
req = requests.get(craftSite).text

edibleData = getCraftingData("Edible_Items", req, [1,2,3,4,5,6])
for edible in edibleData:
    item = [edible[0], 'edible'] #Edible
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

bombData = getCraftingData("Bombs", req, [1,2,3,4,5,6])
for bomb in bombData:
    item = [bomb[0], 'bombs'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

fenceData = getCraftingData("Fences", req, [1,2,3,4,5])
for fence in fenceData:
    item = [fence[0], 'fence'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

sprinklerData = getCraftingData("Sprinklers", req, craftingIndices)
for sprinkler in sprinklerData:
    item = [sprinkler[0], 'sprinkler'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

artisanEquipmentData = getCraftingData("Artisan_Equipment", req, craftingIndices)
for artisanEquipment in artisanEquipmentData:
    item = [artisanEquipment[0], 'artisanequipment'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

fertilizerData = getCraftingData("Fertilizer", req, craftingIndices)
for fertilizer in fertilizerData:
    item = [fertilizer[0], 'fertilizer'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

seedsData = getCraftingData("Seeds", req, craftingIndices)
for seed in seedsData:
    item = [seed[0], 'seed'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

decorData = getCraftingData("Decor", req, craftingIndices)
for decor in decorData:
    item = [decor[0], 'decor'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

fishingData = getCraftingData("Fishing", req, craftingIndices)
for fishing in fishingData:
    item = [fishing[0], 'fishing'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

ringsData = getCraftingData("Rings", req, craftingIndices)
for ring in ringsData:
    item = [ring[0], 'ring'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

consumableData = getCraftingData("Consumables", req, craftingIndices)
for consumable in consumableData:
    item = [consumable[0], 'consumable'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

lightingData = getCraftingData("Lighting", req, craftingIndices)
for lighting in lightingData:
    item = [lighting[0], 'lighting'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

refiningEquipmentData = getCraftingData("Refining_Equipment", req, craftingIndices)
for refiningEquipment in refiningEquipmentData:
    item = [refiningEquipment[0], 'refiningequipment'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

furnitureData = getCraftingData("Furniture", req, craftingIndices)
for furniture in furnitureData:
    item = [furniture[0], 'furniture'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

miscData = getCraftingData("Misc", req, craftingIndices)
for misc in miscData:
    item = [misc[0], 'misc'] 
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

# Artisan Goods
site = "https://stardewvalleywiki.com/Artisan_Goods"
req = requests.get(site).text
columns = ['Name', 'Recipe', 'Time', 'Sell', 'Equipment']
indices = [1, 3, 4, 5]
beeHouseIndices = [1, 2, 4, 6]
caskIndices = [1, 2]

honeyData = getBeeHouseData(req, beeHouseIndices)
item = [honeyData[0], 'artisangood']
df.append(pd.Series(item,index=itemColumns), ignore_index=True)

pressData = getArtisanData("Cheese Press", req, indices)

for product in pressData:
    item = [product[0], 'artisangood']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

kegData = getArtisanData("Keg", req, indices)
for product in kegData:
    item = [product[0], 'artisangood']
    df = df.append(pd.Series(item, index=itemColumns), ignore_index=True)

loomData = getArtisanData("Loom", req, indices)
for product in loomData:
    df = df.append(pd.Series(item,index=itemColumns), ignore_index=True)

mayonnaiseMachineData = getArtisanData("Mayonnaise Machine", req, indices)
for product in mayonnaiseMachineData:
    item = [product[0], 'artisangood']
    df = df.append(pd.Series(item,index=itemColumns), ignore_index=True)

oilMakerData = getOilMakerData(req, indices)
for product in oilMakerData:
    item = [product[0], 'artisangood']
    df = df.append(pd.Series(item,index=itemColumns), ignore_index=True)

preservesJarData = getArtisanData("Preserves Jar", req, indices)
for product in preservesJarData:
    item = [product[0], 'artisangood']
    df = df.append(pd.Series(item,index=itemColumns), ignore_index=True)

# Animal Products
animals = ['Chickens', 'Ducks', 'Rabbits', 'Dinosaurs', 'Cows', 'Goats', 'Sheep', 'Pigs']
site = "https://stardewvalleywiki.com/Animals"
req = requests.get(site).text
for animal in animals:
    foodProductData = getFoodProductData(animal, req, [1,2], [1,2,3])
    for product in foodProductData:
        item = [product[0], 'animalproduct']
        df = df.append(pd.Series(item,index=itemColumns), ignore_index=True)

df.to_csv("/home/amrit/projects/ItemData.csv", index=False, encoding='utf-8')

