select eu.unique_id, e.name
from Employees e
left join EmployeeUni eu
on e.id = eu.id;
