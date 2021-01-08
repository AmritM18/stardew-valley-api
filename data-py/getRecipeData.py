import requests
from bs4 import BeautifulSoup
import pandas as pd

# Data taken from https://stardewvalleywiki.com/Cooking

def getRecipeData(recipeIndices):
    recipeSite = "https://stardewvalleywiki.com/Cooking"
    req = requests.get(recipeSite).text
    req = req.split("id=\"Recipes\"")
    req = req[1]
    soup = BeautifulSoup(req,'lxml')

    table = soup.find('table',{'class':'wikitable'})
    recipeRows = []
    
    rows = table.findChildren('tr', recursive=False)
    for i in range(1, len(rows)):
        tds = rows[i].findChildren('td', recursive=False)

        recipe = [tds[x].text.strip(' ').strip('\n').replace('\xa0', '') for x in recipeIndices]

        # extra formatting for 1,2,3,5   (1,3,4,6 for columns on the webpage)
        bN = recipe[1].count(')') - 1
        recipe[1] = recipe[1].replace(')', '),', bN)

        recipe[2] = recipe[2].replace(' ', ' Energy, ')
        recipe[2] += ' Health'

        bN = recipe[3].count(')') - 1
        recipe[3] = recipe[3].replace(')', '),', bN)
        if i == len(rows)-1: recipe[3] = recipe[3].replace(')', '),') # bad


        recipe[5] = recipe[5].replace('+ ', ' hearts')

        recipeRows.append(recipe)

    return recipeRows

def main():
    # Go to Minerals page and choose the columns you want
    recipeColumns = ["Name", "Ingredients", "Healing", "Buffs", "Duration", "Sources", "Sell"]
    recipeIndices = [1,3,4,5,6,7,8]

    df = pd.DataFrame(columns=recipeColumns)
    recipeRows = getRecipeData(recipeIndices)
    for item in recipeRows:
        df = df.append(pd.Series(item, index=recipeColumns), ignore_index=True)
    
    df.to_csv("/home/amrit/projects/RecipeData.csv", index=False, encoding='utf-8')

if __name__ == "__main__":
    main()