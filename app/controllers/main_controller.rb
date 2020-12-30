class MainController < ApplicationController

  before_action :force_json, only: :villager

  def index; end

  def villager
    @data = Villager.ransack(name_eq: params[:q]).result(distinct: true)
  end

  private

  def force_json
    request.format = :json
  end
end