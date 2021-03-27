select
places.*
, row_to_json(cities) cities
, row_to_json(place_categories) place_categories
, row_to_json(tourism_types) tourism_types
from places
left join cities on places.city_id = cities.id
left join place_categories on places.category_id = place_categories.id
left join tourism_types on places.tourism_type_id = tourism_types.id

