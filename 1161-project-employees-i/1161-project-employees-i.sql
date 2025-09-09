/* Write your PL/SQL query statement below */

select project_id,
round (avg(experience_years), 2) as average_years
from Project
inner join employee
Using (employee_id)
group by project_id