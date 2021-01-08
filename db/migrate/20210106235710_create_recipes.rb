class CreateRecipes < ActiveRecord::Migration[6.0]
  def change
    create_table :recipes do |t|
      t.string :name
      t.string :ingredients
      t.string :healing
      t.string :buffs
      t.string :duration
      t.string :sources
      t.string :sell

      t.timestamps
    end
  end
end
