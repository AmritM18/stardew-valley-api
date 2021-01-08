class MainController < ApplicationController

  before_action :force_json

  def index; end

  def item
    @data = Item.ransack(name_start: params[:q]).result(distinct: true)
  end

  def villager
    @data = Villager.ransack(name_start: params[:q]).result(distinct: true)
  end

  def season
    @data = Season.ransack(name_start: params[:q]).result(distinct: true)
  end

  def crop
    @data = Crop.ransack(name_start: params[:q]).result(distinct: true)
  end

  def fish
    @data = Fish.ransack(name_start: params[:q]).result(distinct: true)
  end

  def forage
    @data = Forage.ransack(name_start: params[:q]).result(distinct: true)
  end

  def mineral
    @data = Mineral.ransack(name_start: params[:q]).result(distinct: true)
  end

  def recipe
    @data = Recipe.ransack(name_start: params[:q]).result(distinct: true)
  end

  def artisanequipment
    @data = ArtisanEquipment.ransack(name_start: params[:q]).result(distinct: true)
  end

  def bomb
    @data = Bomb.ransack(name_start: params[:q]).result(distinct: true)
  end

  def consumable
    @data = Consumable.ransack(name_start: params[:q]).result(distinct: true)
  end
  
  def decor
    @data = Decor.ransack(name_start: params[:q]).result(distinct: true)
  end

  def edible
    @data = Edible.ransack(name_start: params[:q]).result(distinct: true)
  end

  def fence
    @data = Fence.ransack(name_start: params[:q]).result(distinct: true)
  end

  def fertilizer
    @data = Fertilizer.ransack(name_start: params[:q]).result(distinct: true)
  end

  def fishing
    @data = Fishing.ransack(name_start: params[:q]).result(distinct: true)
  end

  def furniture
    @data = Furniture.ransack(name_start: params[:q]).result(distinct: true)
  end

  def lighting
    @data = Lighting.ransack(name_start: params[:q]).result(distinct: true)
  end

  def misc
    @data = Misc.ransack(name_start: params[:q]).result(distinct: true)
  end

  def refiningequipment
    @data = RefiningEquipment.ransack(name_start: params[:q]).result(distinct: true)
  end

  def ring
    @data = Ring.ransack(name_start: params[:q]).result(distinct: true)
  end

  def seed
    @data = Seed.ransack(name_start: params[:q]).result(distinct: true)
  end

  def sprinkler
    @data = Sprinkler.ransack(name_start: params[:q]).result(distinct: true)
  end

  private

  def force_json
    request.format = :json
  end
end