select
trips.*
, row_to_json(list_levels) list_levels
, row_to_json(cities) cities
, row_to_json(trip_categories) trip_categories
, row_to_json(tourism_types) tourism_types
, row_to_json(list_seasons) list_seasons
from trips
left join list_levels on trips.level_id = list_levels.id
left join cities on trips.city_id = cities.id
left join trip_categories on trips.category_id = trip_categories.id
left join tourism_types on trips.tourism_type_id = tourism_types.id
left join list_seasons on trips.season_id = list_seasons.id

