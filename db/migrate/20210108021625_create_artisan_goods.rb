class CreateArtisanGoods < ActiveRecord::Migration[6.0]
  def change
    create_table :artisan_goods do |t|
      t.string :name
      t.string :recipe
      t.string :time
      t.string :sell
      t.string :equipment

      t.timestamps
    end
  end
end
