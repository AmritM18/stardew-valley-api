json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.gifts item.gifts
    json.birthday item.birthday
    json.address item.address
  end
end