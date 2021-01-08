json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.description item.description
    json.recipe item.recipe
    json.energy item.energy
    json.health item.health
    json.source item.source
  end
end