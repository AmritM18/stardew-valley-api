class CreateSprinklers < ActiveRecord::Migration[6.0]
  def change
    create_table :sprinklers do |t|
      t.string :name
      t.string :description
      t.string :recipe
      t.string :source

      t.timestamps
    end
  end
end
