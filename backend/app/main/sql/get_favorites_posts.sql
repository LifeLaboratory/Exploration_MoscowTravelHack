select
  *
from
  places
where
  id = any(array(
    select
      favoritable_id
    from
      favorites
    where
      "user_id" = {id_user}::int
  ))