class MainController < ApplicationController

  before_action :force_json

  def index; end

  def item
    @data = Item.ransack(name_eq: params[:q]).result(distinct: true)
  end

  def villager
    @data = Villager.ransack(name_eq: params[:q]).result(distinct: true)
  end

  def season
    @data = Season.ransack(name_eq: params[:q]).result(distinct: true)
  end

  def crop
    @data = Crop.ransack(name_eq: params[:q]).result(distinct: true)
  end

  def fish
    @data = Fish.ransack(name_eq: params[:q]).result(distinct: true)
  end

  def forage
    @data = Forage.ransack(name_eq: params[:q]).result(distinct: true)
  end

  private

  def force_json
    request.format = :json
  end
end