class CreateForages < ActiveRecord::Migration[6.0]
  def change
    create_table :forages do |t|
      t.string :name
      t.string :season_name
      t.string :location
      t.string :sell
      t.string :uses
      t.references :season, null: false, foreign_key: true

      t.timestamps
    end
  end
end
