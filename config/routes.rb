Rails.application.routes.draw do
  get "/", to: "home#index"

  get :villager, controller: :main
end
