/* Write your PL/SQL query statement below */
/* tabela Activity */
/* vai ter que ser usado o TO_CHAR(MIN(event_date), 'YYYY-MM-DD') - output somente considerando data e nao hora. Se utilizar somente o MIN, sai a hora no output 00:00:00. */

SELECT player_id,
       TO_CHAR(MIN(event_date), 'YYYY-MM-DD') AS first_login
FROM Activity
GROUP BY player_id;



