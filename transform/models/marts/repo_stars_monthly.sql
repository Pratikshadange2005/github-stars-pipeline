select distinct
  repo_id,
  repo_name,
  date_trunc('month', event_date) as date_month,
  count(*) as star_count,
  sum(count(*)) over (partition by repo_id order by date_trunc('month', event_date)) as cumul_star_count
from {{ ref("stg_gharchive") }}
where event_type = 'Watch'
group by repo_id, repo_name, date_month
