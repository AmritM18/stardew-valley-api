Rails.application.routes.draw do
  get "/", to: "home#index"
  get "/help", to: "home#help"

  get :item, controller: :main

  get :villager, controller: :main
  get :crop, controller: :main
  get :season, controller: :main
  get :fish, controller: :main
  get :forage, controller: :main
end
