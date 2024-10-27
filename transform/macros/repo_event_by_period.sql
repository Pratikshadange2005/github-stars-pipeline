{% macro repo_event_by_period(event_type, period) -%}
select distinct
  repo_id,
  repo_name,
  date_trunc('{{ period }}', event_date) as date_{{ period }},
  count(*) as {{ event_type }}_count,
  sum({{ event_type }}_count) over (partition by repo_id order by date_{{ period }}) as cumul_{{ event_type }}_count
from {{ ref("stg_gharchive") }}
where event_type = '{{ event_type | capitalize }}'
group by 1, 2, 3
{%- endmacro %}
