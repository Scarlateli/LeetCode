/* Write your PL/SQL query statement below */
select contest_id, round(count(R.contest_id)*100 / (select count(*)
from Users), 2) percentage from Register R group by contest_id
order by percentage desc, contest_id