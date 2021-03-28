select
  *
from
  favorites
where
  "user_id" = {id_user}::int
  and favoritable_id = {favoritable_id}