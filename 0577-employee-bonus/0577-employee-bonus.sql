/* Write your PL/SQL query statement below */
/* tabela --> Employee */
/* tabela --> Bonus */

SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;

