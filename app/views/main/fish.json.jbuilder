json.data do
  json.array!(@data) do |item|
    json.name item.name
    json.season item.season_name
    json.sell item.sell
    json.location item.location
    json.time item.time
    json.weather item.weather
    json.difficulty item.difficulty
    json.uses item.uses
  end
end