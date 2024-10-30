select
  case
    when lower(replace(type, 'Event', '')) = 'push' then 'commit'
    when lower(replace(type, 'Event', '')) = 'watch' then 'star'
    else lower(replace(type, 'Event', ''))
  end as event_type,
  actor.login as user,
  repo.id as repo_id,
  repo.name as repo_name,
  created_at as event_date
from {{ source("gharchive", "src_gharchive") }}



