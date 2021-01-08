json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.ingredients item.ingredients
    json.healing item.healing
    json.buffs item.buffs
    json.duration item.duration
    json.sources item.sources
    json.sell item.sell
  end
end