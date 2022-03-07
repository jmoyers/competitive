# Write your MySQL query statement below
select
  ifnull(round(avg(a.cnt), 2), 0.00) as average_sessions_per_user
from
(select 
  user_id,
  count(distinct(session_id)) as cnt
from activity 
where 
  activity_date >= DATE_SUB("2019-07-27", interval 29 day) and
  activity_date <= "2019-07-27" 
group by user_id) as a;
