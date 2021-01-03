class MainController < ApplicationController

  before_action :force_json

  def index; end

  def villager
    @data = Villager.ransack(villager_eq: params[:q]).result(distinct: true)
  end

  def season
    @data = Season.ransack(season_eq: params[:q]).result(distinct: true)
  end

  def crop
    @data = Crop.ransack(crop_eq: params[:q]).result(distinct: true)
  end

  private

  def force_json
    request.format = :json
  end
end