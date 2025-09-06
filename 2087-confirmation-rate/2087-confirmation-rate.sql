select s.user_id,
round(sum(case when C.action= 'confirmed' then 1 else 0 End)/ count(s.user_id),2) as Confirmation_rate
from Signups s 
left join Confirmations C
on s.user_id = C.user_id
group by s.user_id
order by Confirmation_rate;