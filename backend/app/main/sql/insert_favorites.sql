insert into favorites("user_id", "favoritable_id", "favoritable_type")
  values ({id_user}::int, {id_post}::int, {type}::text)