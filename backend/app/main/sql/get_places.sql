with places_info as (
select
places.*
, row_to_json(cities) cities
, row_to_json(place_categories) place_categories
, row_to_json(tourism_types) tourism_types
from places
left join cities on places.city_id = cities.id
left join place_categories on places.category_id = place_categories.id
left join tourism_types on places.tourism_type_id = tourism_types.id
),
tags as (
select

places.id
, array_agg(t) array_tags
from places_info places
join place_tag pt on places.id = pt.place_id
join tags t on pt.tag_id = t.id
group by places.id
)
select
places_info.*
, array_to_json(tags.array_tags) "tags"
, google_ratings.rating google_rating
from
places_info
left join tags on tags.id = places_info.id
left join google_ratings on places_info.id = google_ratings.id

order by
  google_rating desc -- По оценке мировой
  , created_at desc  -- Даем свежие
