# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
require 'csv'

character_info = File.read(Rails.root.join('lib', 'seeds', 'CharacterModelInfo.csv'))
character = CSV.parse(character_info, :headers => true, :encoding => 'ISO-8859-1')
character.each do |row|
    c = Villager.new
    c.name = row['Villager']
    c.gifts = row['Gifts']
    c.birthday = row['Birthday']
    c.address = row['Address']
    c.save
    puts "#{c.name}, #{c.gifts} saved"
    # puts row.to_hash
end

puts "There are now #{Villager.count} rows in the villagers table"
  