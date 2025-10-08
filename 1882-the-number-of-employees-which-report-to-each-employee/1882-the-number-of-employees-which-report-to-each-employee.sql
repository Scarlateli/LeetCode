/* Write your PL/SQL query statement below */
-- considerar um manager um employee que tem pelo menos 1 employee se reportando a ele
-- retornar os ids e nomes de todos os managers
-- retornar o numero de employees que reportam diretamente par os gerentes
-- e a media (AVG) de tempo(idade) arredondado
-- ordernar por employee_id

select e.employee_id,e.name,count(e1.employee_id)"reports_count"
,round(avg(e1.age))"average_age"
from employees e join employees e1
on e.employee_id =e1.reports_to
group by e.employee_id,e.name
order by employee_id;
