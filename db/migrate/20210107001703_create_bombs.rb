class CreateBombs < ActiveRecord::Migration[6.0]
  def change
    create_table :bombs do |t|
      t.string :name
      t.string :description
      t.string :recipe
      t.string :radius
      t.string :source
      t.string :sell

      t.timestamps
    end
  end
end
