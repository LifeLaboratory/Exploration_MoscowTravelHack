insert
into
tags
(title)

select
*
from unnest(
array{titles}
)
returning *