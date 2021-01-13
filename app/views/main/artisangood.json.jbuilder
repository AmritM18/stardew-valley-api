json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.recipe item.recipe
    json.time item.time
    json.sell item.sell
    json.equipment item.equipment
  end
end