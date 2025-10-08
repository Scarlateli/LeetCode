/* Write your PL/SQL query statement below */
-- considerar um manager um employee que tem pelo menos 1 employee se reportando a ele
-- retornar os ids e nomes de todos os managers
-- retornar o numero de employees que reportam diretamente par os gerentes
-- e a media (AVG) de tempo(idade) arredondado
-- ordernar por employee_id

select e.employee_id, e.name, manager.reports_count, manager.average_age
from Employees e
join(
    select reports_to, count(reports_to) reports_count, round(avg(age), 0) average_age
    from Employees
    group by reports_to
) manager 
on e.employee_id = manager.reports_to
order by e.employee_id

