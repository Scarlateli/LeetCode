/* Write your PL/SQL query statement below */
select p.product_name, s.year, s.price
from sales s
left join product p
on p.product_id = s.product_id
