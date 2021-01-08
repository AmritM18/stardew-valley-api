class CreateMinerals < ActiveRecord::Migration[6.0]
  def change
    create_table :minerals do |t|
      t.string :name
      t.string :sell
      t.string :location
      t.string :uses

      t.timestamps
    end
  end
end
