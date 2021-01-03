json.data do
  json.array!(@data) do |item|
    json.name item.crop
    json.season item.szn
    json.buy item.buy
    json.sell item.sell
    json.growth item.growth
    json.healing item.healing
  end
end