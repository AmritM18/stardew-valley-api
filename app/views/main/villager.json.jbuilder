json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.birthday item.birthday
    json.loves item.loves
    json.likes item.likes
    json.neutral item.neutral
    json.dislikes item.dislikes
    json.hates item.hates
  end
end