select id, title from tags
where title = any(array{titles})