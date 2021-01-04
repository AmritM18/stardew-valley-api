json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.crops item.crops
    json.forages item.forages
    json.fish item.fish
  end
end