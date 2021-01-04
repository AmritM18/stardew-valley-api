json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.category item.category
  end
end