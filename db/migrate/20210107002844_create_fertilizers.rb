class CreateFertilizers < ActiveRecord::Migration[6.0]
  def change
    create_table :fertilizers do |t|
      t.string :name
      t.string :description
      t.string :recipe
      t.string :source

      t.timestamps
    end
  end
end
