with user_posts as (
  select
   id_post
   , case when percent > 60 then True else False end success
  from
    user_history
  where
    id_user = {id_user}
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
        place_id = any(array(select id_post from user_posts where success is true))
      group by tag_id
    ) as get_post_tegs
    order by 2
    limit 10
)
select
   tags.title
 from
 rank_tags
 join tags on tags.id = rank_tags.tag_id
 order by tag_index
