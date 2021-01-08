class CreateEdibles < ActiveRecord::Migration[6.0]
  def change
    create_table :edibles do |t|
      t.string :name
      t.string :description
      t.string :recipe
      t.string :energy
      t.string :health
      t.string :source

      t.timestamps
    end
  end
end
