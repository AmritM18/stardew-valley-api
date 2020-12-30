class CreateVillagers < ActiveRecord::Migration[6.0]
  def change
    create_table :villagers do |t|
      t.string :name
      t.string :gifts
      t.string :birthday
      t.string :address

      t.timestamps
    end
  end
end
