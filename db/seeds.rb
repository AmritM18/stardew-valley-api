# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
require 'csv'

villager_info = File.read(Rails.root.join('lib', 'seeds', 'VillagerData.csv'))
villager = CSV.parse(villager_info, :headers => true, :encoding => 'ISO-8859-1')

villager.each do |row|
    v = Villager.new
    v.villager = row['Villager']
    v.birthday = row['Birthday']
    v.loves = row['Loves']
    v.likes = row['Likes']
    v.neutral = row['Neutral']
    v.dislikes = row['Dislikes']
    v.hates = row['Hates']
    v.save
    puts "Added #{v.villager} with season #{v.loves}"
end
puts "There are now #{Villager.count} rows in the villagers table"

# Our convention is Spring (0), Summer (1), Fall (2), Winter (3)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasons.each do |season| 
    s = Season.new
    s.season = season
    s.save
end
puts "There are now #{Season.count} rows in the seasons table"

crop_info = File.read(Rails.root.join('lib', 'seeds', 'CropData.csv'))
crop = CSV.parse(crop_info, :headers => true, :encoding => 'ISO-8859-1')

crop.each do |row|
    season = Season.where(season: row['Season']).first.id
    puts season
    c = Crop.new
    c.crop = row['Crop']
    c.szn = row['Season']
    c.buy = row['Seed Price']
    c.sell = row['Sell Prices']
    c.growth = row['Growth Time']
    c.healing = row['Healing']
    c.season_id = season
    c.save
    puts "Added #{c.crop} with season #{c.szn}"
end
puts "There are now #{Crop.count} rows in the crops table"