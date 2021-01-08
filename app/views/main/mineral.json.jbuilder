json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.sell item.sell
    json.location item.location
    json.uses item.uses
  end
end