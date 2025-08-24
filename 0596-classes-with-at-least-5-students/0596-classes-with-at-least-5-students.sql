SELECT class
FROM (
    SELECT class, COUNT(*) AS total
    FROM courses
    GROUP BY class
) t
WHERE total >= 5;
