Select distinct
  repo_id,
  repo_name,
  date_trunc(‘day’, created_at) as date_day,
  count(*) as star_count
from {{ ref("stg_gharchive") }}
where type = ‘WatchEvent’
