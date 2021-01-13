json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.sell item.sell
    json.animal item.animal
    json.cost item.cost
    json.requirement item.requirement
  end
end