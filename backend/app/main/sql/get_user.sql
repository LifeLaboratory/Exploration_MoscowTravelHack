select
  id
from users
where
  "sign_hash" = '{sign_hash}'::text
