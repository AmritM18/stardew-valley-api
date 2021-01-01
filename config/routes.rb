Rails.application.routes.draw do
  get "/", to: "home#index"
  get "/help", to: "home#help"

  get :villager, controller: :main
end
