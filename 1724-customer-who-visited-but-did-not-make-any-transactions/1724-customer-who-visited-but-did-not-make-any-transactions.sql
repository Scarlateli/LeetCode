select customer_id, count(V.visit_id) 
as count_no_trans 
from Visits V 
left join Transactions T 
on T.visit_id = V.visit_id 
where T.visit_id is null 
group by customer_id