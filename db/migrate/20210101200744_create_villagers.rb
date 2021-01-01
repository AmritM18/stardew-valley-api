class CreateVillagers < ActiveRecord::Migration[6.0]
  def change
    create_table :villagers do |t|
      t.string :villager
      t.string :birthday
      t.string :loves
      t.string :likes
      t.string :neutral
      t.string :dislikes
      t.string :hates

      t.timestamps
    end
  end
end
