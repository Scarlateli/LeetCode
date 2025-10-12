select employee_id, department_id
from employee
where primary_flag = 'Y'
or (primary_flag = 'N'
and employee_id not in (
    select employee_id
    from employee
    where primary_flag = 'Y'
));