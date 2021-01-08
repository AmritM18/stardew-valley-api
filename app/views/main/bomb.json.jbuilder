json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.description item.description
    json.recipe item.recipe
    json.radius item.radius
    json.source item.source
    json.sell item.sell
  end
end