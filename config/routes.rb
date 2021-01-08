Rails.application.routes.draw do
  get "/", to: "home#index"
  get "/help", to: "home#help"

  get :item, controller: :main

  get :villager, controller: :main
  get :crop, controller: :main
  get :season, controller: :main
  get :fish, controller: :main
  get :forage, controller: :main

  get :mineral, controller: :main
  get :recipe, controller: :main

  get :artisanequipment, controller: :main
  get :bomb, controller: :main
  get :consumable, controller: :main
  get :decor, controller: :main
  get :edible, controller: :main
  get :fence, controller: :main
  get :fertilizer, controller: :main
  get :fishing, controller: :main
  get :furniture, controller: :main
  get :lighting, controller: :main
  get :misc, controller: :main
  get :refiningequipment, controller: :main
  get :ring, controller: :main
  get :seed, controller: :main
  get :sprinkler, controller: :main
end
