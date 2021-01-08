class CreateFences < ActiveRecord::Migration[6.0]
  def change
    create_table :fences do |t|
      t.string :name
      t.string :description
      t.string :life
      t.string :recipe
      t.string :source

      t.timestamps
    end
  end
end
