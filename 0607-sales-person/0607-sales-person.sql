/* Write your PL/SQL query statement below */
select name
from salesperson
where name not in (
    select S.name
    from salesperson S, company C, Orders O 
    where S.sales_id = O.sales_id
      and C.com_id = O.com_id 
      and C.name = 'RED'
);

