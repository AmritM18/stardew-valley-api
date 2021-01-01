class CreateCrops < ActiveRecord::Migration[6.0]
  def change
    create_table :crops do |t|
      t.string :crop
      t.string :szn
      t.string :buy
      t.string :sell
      t.string :growth
      t.string :healing
      t.references :season, null: false, foreign_key: true

      t.timestamps
    end
  end
end
