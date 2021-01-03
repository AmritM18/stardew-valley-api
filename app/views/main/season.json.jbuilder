json.data do
  json.array!(@data) do |item|
    json.name item.season
    json.crops item.crops
  end
end