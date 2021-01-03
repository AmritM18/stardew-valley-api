class CreateCrops < ActiveRecord::Migration[6.0]
  def change
    create_table :crops do |t|
      t.string :name
      t.string :season_name
      t.string :buy
      t.string :sell
      t.string :growth
      t.string :healing
      t.references :season, null: false, foreign_key: true

      t.timestamps
    end
  end
end
