select distinct
  repo_id,
  repo_name,
  date_trunc('day', event_date) as date_day,
  count(*) as push_count,
  sum(push_count) over (partition by repo_id order by date_day) as cumul_push_count
from {{ ref("stg_gharchive") }}
where event_type = 'Push'
group by 1, 2, 3