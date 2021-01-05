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