-- TODO: обязательные поля
insert into users("name", "email", "password", "api_token", "sign_hash")
  values ({sign_hash}::text, {sign_hash}::text, {sign_hash}::text, {sign_hash}::text, {sign_hash}::text)