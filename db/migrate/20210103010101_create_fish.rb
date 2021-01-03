class CreateFish < ActiveRecord::Migration[6.0]
  def change
    create_table :fish do |t|
      t.string :name
      t.string :season_name
      t.string :sell
      t.string :location
      t.string :time
      t.string :weather
      t.string :difficulty
      t.string :uses
      t.references :season, null: false, foreign_key: true

      t.timestamps
    end
  end
end
