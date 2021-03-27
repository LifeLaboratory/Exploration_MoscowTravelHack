select
events.*
, row_to_json(cities) cities
, row_to_json(places) places
, row_to_json(event_categories) event_categories
, row_to_json(tourism_types) tourism_types
, row_to_json(list_seasons) list_seasons
from events
left join cities on cities.id = events.city_id
left join places on places.id = events.place_id
left join event_categories on event_categories.id = events.category_id
left join tourism_types on tourism_types.id = events.tourism_type_id
left join list_seasons on list_seasons.id = events.season_id