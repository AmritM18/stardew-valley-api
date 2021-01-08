# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `rails
# db:schema:load`. When creating a new database, `rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2021_01_08_021640) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "animal_products", force: :cascade do |t|
    t.string "name"
    t.string "sell"
    t.string "animal"
    t.string "cost"
    t.string "requirement"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "artisan_equipments", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "artisan_goods", force: :cascade do |t|
    t.string "name"
    t.string "recipe"
    t.string "time"
    t.string "sell"
    t.string "equipment"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "bombs", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "radius"
    t.string "source"
    t.string "sell"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "consumables", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "crops", force: :cascade do |t|
    t.string "name"
    t.string "season_name"
    t.string "buy"
    t.string "sell"
    t.string "growth"
    t.string "healing"
    t.bigint "season_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["season_id"], name: "index_crops_on_season_id"
  end

  create_table "decors", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "edibles", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "energy"
    t.string "health"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "fences", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "life"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "fertilizers", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "fish", force: :cascade do |t|
    t.string "name"
    t.string "season_name"
    t.string "sell"
    t.string "location"
    t.string "time"
    t.string "weather"
    t.string "difficulty"
    t.string "uses"
    t.bigint "season_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["season_id"], name: "index_fish_on_season_id"
  end

  create_table "fishings", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "forages", force: :cascade do |t|
    t.string "name"
    t.string "season_name"
    t.string "location"
    t.string "sell"
    t.string "uses"
    t.bigint "season_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["season_id"], name: "index_forages_on_season_id"
  end

  create_table "furnitures", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "items", force: :cascade do |t|
    t.string "name"
    t.string "category"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "lightings", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "minerals", force: :cascade do |t|
    t.string "name"
    t.string "sell"
    t.string "location"
    t.string "uses"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "miscs", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "recipes", force: :cascade do |t|
    t.string "name"
    t.string "ingredients"
    t.string "healing"
    t.string "buffs"
    t.string "duration"
    t.string "sources"
    t.string "sell"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "refining_equipments", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "rings", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "seasons", force: :cascade do |t|
    t.string "name"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "seeds", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "sprinklers", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "recipe"
    t.string "source"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "villagers", force: :cascade do |t|
    t.string "name"
    t.string "birthday"
    t.string "loves"
    t.string "likes"
    t.string "neutral"
    t.string "dislikes"
    t.string "hates"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  add_foreign_key "crops", "seasons"
  add_foreign_key "fish", "seasons"
  add_foreign_key "forages", "seasons"
end
