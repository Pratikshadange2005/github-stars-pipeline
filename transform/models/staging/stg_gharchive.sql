select
  -- Convert event type to lowercase and replace specific values
  case
    when LOWER(REPLACE(type, 'Event', '')) = 'push' then 'commit'
    when LOWER(REPLACE(type, 'Event', '')) = 'watch' then 'star'
    else LOWER(REPLACE(type, 'Event', ''))
  end as event_type,
  
  actor.login as user,
  repo.id as repo_id,
  repo.name as repo_name,
  created_at as event_date
from {{ source("gharchive", "src_gharchive") }}



