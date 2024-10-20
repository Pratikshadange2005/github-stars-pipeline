select distinct
  repo_id,
  repo_name,
  date_trunc('day', event_date) as date_day,
  count(*) as push_count,
  sum(count(*)) over (partition by repo_id order by date_trunc('day', event_date)) as cumul_push_count
from {{ ref("stg_gharchive") }}
where event_type = 'Push'
group by repo_id, repo_name, date_day
