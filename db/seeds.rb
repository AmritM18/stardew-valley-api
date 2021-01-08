# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
require 'csv'

item_info = File.read(Rails.root.join('lib', 'seeds', 'ItemData.csv'))
item = CSV.parse(item_info, :headers => true, :encoding => 'ISO-8859-1')

item.each do |row|
    i = Item.new
    i.name = row['Item']
    i.category = row['Category']
    i.save
end
puts "There are now #{Item.count} rows in the items table"

villager_info = File.read(Rails.root.join('lib', 'seeds', 'VillagerData.csv'))
villager = CSV.parse(villager_info, :headers => true, :encoding => 'ISO-8859-1')

villager.each do |row|
    v = Villager.new
    v.name = row['Villager']
    v.birthday = row['Birthday']
    v.loves = row['Loves']
    v.likes = row['Likes']
    v.neutral = row['Neutral']
    v.dislikes = row['Dislikes']
    v.hates = row['Hates']
    v.save
    puts "Added #{v.name} with season #{v.loves}"
end
puts "There are now #{Villager.count} rows in the villagers table"

# Our convention is Spring (0), Summer (1), Fall (2), Winter (3)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasons.each do |season| 
    s = Season.new
    s.name = season
    s.save
end
puts "There are now #{Season.count} rows in the seasons table"

crop_info = File.read(Rails.root.join('lib', 'seeds', 'CropData.csv'))
crop = CSV.parse(crop_info, :headers => true, :encoding => 'ISO-8859-1')

crop.each do |row|
    season = Season.where(name: row['Season']).first.id
    c = Crop.new
    c.name = row['Crop']
    c.season_name = row['Season']
    c.buy = row['Seed Price']
    c.sell = row['Sell Prices']
    c.growth = row['Growth Time']
    c.healing = row['Healing']
    c.season_id = season
    c.save
    puts "Added #{c.name} with season #{c.season_name}"
end
puts "There are now #{Crop.count} rows in the crops table"

forage_info = File.read(Rails.root.join('lib', 'seeds', 'ForageData.csv'))
forage = CSV.parse(forage_info, :headers => true, :encoding => 'ISO-8859-1')

forage.each do |row|
    season = Season.where(name: row['Season']).first.id
    f = Forage.new
    f.name = row['Forage']
    f.season_name = row['Season']
    f.location = row['Location']
    f.sell = row['Sell']
    f.uses = row['Uses']
    f.season_id = season
    f.save
    puts "Added #{f.name} with season #{f.season_name}"
end
puts "There are now #{Forage.count} rows in the forages table"

fish_info = File.read(Rails.root.join('lib', 'seeds', 'FishData.csv'))
fish = CSV.parse(fish_info, :headers => true, :encoding => 'ISO-8859-1')

fish.each do |row|
    season = Season.where(name: row['Season']).first.id
    f = Fish.new
    f.name = row['Fish']
    f.season_name = row['Season']
    f.location = row['Location']
    f.sell = row['Sell']
    f.time = row['Time']
    f.weather = row['Weather']
    f.difficulty = row['Difficulty']
    f.uses = row['Uses']
    f.season_id = season
    f.save
    puts "Added #{f.name} with season #{f.season_name}"
end
puts "There are now #{Fish.count} rows in the fish table"

mineral_info = File.read(Rails.root.join('lib', 'seeds', 'MineralData.csv'))
mineral = CSV.parse(mineral_info, :headers => true, :encoding => 'ISO-8859-1')

mineral.each do |row|
    f = Mineral.new
    f.name = row['Name']
    f.sell = row['Sell']
    f.location = row['Location']
    f.uses = row['Uses']
    f.save
    puts "Added #{f.name} with location #{f.location}"
end
puts "There are now #{Mineral.count} rows in the mineral table"

recipe_info = File.read(Rails.root.join('lib', 'seeds', 'RecipeData.csv'))
recipe = CSV.parse(recipe_info, :headers => true, :encoding => 'ISO-8859-1')

recipe.each do |row|
    f = Recipe.new
    f.name = row['Name']
    f.ingredients = row['Ingredients']
    f.healing = row['Healing']
    f.buffs = row['Buffs']
    f.duration = row['Duration']
    f.sources = row['Sources']
    f.sell = row['Sell']
    f.save
    puts "Added #{f.name} with ingredients #{f.ingredients}"
end
puts "There are now #{Recipe.count} rows in the recipe table"

artisanequipment_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_ArtisanEquipmentData.csv'))
artisanequipment = CSV.parse(artisanequipment_info, :headers => true, :encoding => 'ISO-8859-1')

artisanequipment.each do |row|
    f = ArtisanEquipment.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{ArtisanEquipment.count} rows in the artisanequipment table"

bomb_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_BombsData.csv'))
bomb = CSV.parse(bomb_info, :headers => true, :encoding => 'ISO-8859-1')

bomb.each do |row|
    f = Bomb.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.radius = row['Radius']
    f.source = row['Source']
    f.sell = row['Sell']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Bomb.count} rows in the bomb table"

seed_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_SeedData.csv'))
seed = CSV.parse(seed_info, :headers => true, :encoding => 'ISO-8859-1')

seed.each do |row|
    f = Seed.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Seed.count} rows in the seed table"

sprinkler_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_SprinklerData.csv'))
sprinkler = CSV.parse(sprinkler_info, :headers => true, :encoding => 'ISO-8859-1')

sprinkler.each do |row|
    f = Sprinkler.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Sprinkler.count} rows in the sprinkler table"

misc_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_MiscData.csv'))
misc = CSV.parse(misc_info, :headers => true, :encoding => 'ISO-8859-1')

misc.each do |row|
    f = Misc.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Misc.count} rows in the misc table"

ring_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_RingsData.csv'))
ring = CSV.parse(ring_info, :headers => true, :encoding => 'ISO-8859-1')

ring.each do |row|
    f = Ring.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Ring.count} rows in the ring table"

refiningequipment_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_RefiningEquipmentData.csv'))
refiningequipment = CSV.parse(refiningequipment_info, :headers => true, :encoding => 'ISO-8859-1')

refiningequipment.each do |row|
    f = RefiningEquipment.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{RefiningEquipment.count} rows in the refiningequipment table"

lighting_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_LightingData.csv'))
lighting = CSV.parse(lighting_info, :headers => true, :encoding => 'ISO-8859-1')

lighting.each do |row|
    f = Lighting.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Lighting.count} rows in the lighting table"

fertilizer_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_FertilizerData.csv'))
fertilizer = CSV.parse(fertilizer_info, :headers => true, :encoding => 'ISO-8859-1')

fertilizer.each do |row|
    f = Fertilizer.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Fertilizer.count} rows in the fertilizer table"

furniture_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_FurnitureData.csv'))
furniture = CSV.parse(furniture_info, :headers => true, :encoding => 'ISO-8859-1')

furniture.each do |row|
    f = Furniture.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Furniture.count} rows in the furniture table"

fishing_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_FishingData.csv'))
fishing = CSV.parse(fishing_info, :headers => true, :encoding => 'ISO-8859-1')

fishing.each do |row|
    f = Fishing.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Fishing.count} rows in the fishing table"

consumable_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_ConsumableData.csv'))
consumable = CSV.parse(consumable_info, :headers => true, :encoding => 'ISO-8859-1')

consumable.each do |row|
    f = Consumable.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Consumable.count} rows in the consumable table"

fence_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_FencesData.csv'))
fence = CSV.parse(fence_info, :headers => true, :encoding => 'ISO-8859-1')

fence.each do |row|
    f = Fence.new
    f.name = row['Name']
    f.description = row['Description']
    f.life = row['Life']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Fence.count} rows in the fence table"

edible_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_EdibleData.csv'))
edible = CSV.parse(edible_info, :headers => true, :encoding => 'ISO-8859-1')

edible.each do |row|
    f = Edible.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.energy = row['Energy']
    f.health = row['Health']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Edible.count} rows in the edible table"

decor_info = File.read(Rails.root.join('lib', 'seeds', 'Crafting_DecorData.csv'))
decor = CSV.parse(decor_info, :headers => true, :encoding => 'ISO-8859-1')

decor.each do |row|
    f = Decor.new
    f.name = row['Name']
    f.description = row['Description']
    f.recipe = row['Recipe']
    f.source = row['Source']
    f.save
    puts "Added #{f.name} with description #{f.description}"
end
puts "There are now #{Decor.count} rows in the decor table"

artisan_goods_info = File.read(Rails.root.join('lib', 'seeds', 'ArtisanData.csv'))
artisan_good = CSV.parse(artisan_goods_info, :headers => true, :encoding => 'ISO-8859-1')

artisan_good.each do |row|
    f = ArtisanGood.new
    f.name = row['Name']
    f.recipe = row['Recipe']
    f.time = row['Time']
    f.sell = row['Sell']
    f.equipment = row['Equipment']
    f.save
    puts "Added #{f.name}"
end
puts "There are now #{ArtisanGood.count} rows in the artisan good table"

animal_product_info = File.read(Rails.root.join('lib', 'seeds', 'AnimalProductData.csv'))
animal_product = CSV.parse(animal_product_info, :headers => true, :encoding => 'ISO-8859-1')

animal_product.each do |row|
    f = AnimalProduct.new
    f.name = row['Name']
    f.sell = row['Sell']
    f.animal = row['Animal']
    f.cost = row['Cost']
    f.requirement = row['Requirement']
    f.save
    puts "Added #{f.name}"
end
puts "There are now #{AnimalProduct.count} rows in the animal product table"
