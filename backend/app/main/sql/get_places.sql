with user_posts as (
  with user_stor as (
    select
     id_post
     , case when percent > 60 then True else False end success
     , true as user_stories
    from
      user_history
    where
      id_user = {id_user}
  ),
   count_user_story as (
    select
      count(1) as count_story
    from
      user_stor
  )
  select
    id_post
    , success
    , user_stories
  from
    user_stor
  union
  select
   id_post
   , case when percent > 60 then True else False end success
   , false as user_stories
  from
    user_history uh
  where (table count_user_story) = 0

),
rank_tags as (
  select
    tag_id
    , row_number() over(order by count_tags desc) as tag_index
  from
    (
      select
        tag_id
        , count(1) as count_tags
      from
        place_tag
      where
        place_id = any(array(select distinct id_post from user_posts where success is true))
      group by tag_id
    ) as get_post_tegs
    order by 2
    limit 10
),

relative_posts as (
  select
  distinct
    place_id
     , min(rt.tag_index) tag_index
  from
    place_tag pt
  join rank_tags rt using(tag_id)
  where
   not(place_id = any(array(select distinct id_post from user_posts where user_stories is true)))
  group by place_id

),
get_posts as (
  select
    p.*
    , row_to_json(cities) cities
    , row_to_json(place_categories) place_categories
    , row_to_json(tourism_types) tourism_types
    , coalesce(rp.tag_index,  (select max(tag_index) from rank_tags ) + 1) tag_index
  from
    places p
  left join relative_posts rp on rp.place_id = p.id
  join cities on p.city_id = cities.id {cities_condition}
  join place_categories on p.category_id = place_categories.id {category_condition}
  join tourism_types on p.tourism_type_id = tourism_types.id {tourism_condition}
)
, tags as (
select

places.id
, array_agg(t) array_tags
from get_posts places
join place_tag pt on places.id = pt.place_id
join tags t on pt.tag_id = t.id
group by places.id
),
places_order_info as (
select
get_posts.*
, array_to_json(tags.array_tags) "tags"
, google_ratings.rating google_rating
, case when user_history.id is not null then 1 else 0 end reading_sort
from
get_posts
left join tags on tags.id = get_posts.id
left join google_ratings on get_posts.id = google_ratings.id
left join user_history on user_history.id_user = {id_user} and user_history.id_post = get_posts.id and type = 'place'
)

select * from places_order_info
order by
    reading_sort       -- Сначала не прочитанные
  , tag_index          -- По интересам пользователя
  , google_rating desc -- По оценке мировой
  , created_at desc    -- Даем свежие
limit 100
