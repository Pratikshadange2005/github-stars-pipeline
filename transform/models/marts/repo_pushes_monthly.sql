select distinct
  repo_id,
  repo_name,
  date_trunc('month', event_date) as date_month,
  count(*) as push_count,
  sum(push_count) over (partition by repo_id order by date_month) as cumul_push_count
from {{ ref("stg_gharchive") }}
where event_type = 'Push'
group by 1, 2, 3
