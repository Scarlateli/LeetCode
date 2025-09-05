/* Write your PL/SQL query statement below */
/*SELECT 
    machine_id,
    ROUND(
        (SUM(CASE WHEN activity_type = 'end' THEN timestamp ELSE 0 END) - 
         SUM(CASE WHEN activity_type = 'start' THEN timestamp ELSE 0 END)) / 
        COUNT(DISTINCT process_id), 
        3
    ) AS processing_time
FROM Activity
GROUP BY machine_id;*/

SELECT 
    s.machine_id,
    ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time
FROM Activity s
JOIN Activity e ON s.machine_id = e.machine_id 
                AND s.process_id = e.process_id
WHERE s.activity_type = 'start' 
  AND e.activity_type = 'end'
GROUP BY s.machine_id
ORDER BY s.machine_id;