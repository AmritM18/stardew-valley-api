class CreateAnimalProducts < ActiveRecord::Migration[6.0]
  def change
    create_table :animal_products do |t|
      t.string :name
      t.string :sell
      t.string :animal
      t.string :cost
      t.string :requirement

      t.timestamps
    end
  end
end
