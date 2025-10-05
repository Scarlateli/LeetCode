/* Write your PL/SQL query statement below */
-- numero unico aparece uma vez na tabela -> select distinct
-- achar o maior numero possivel na tabela
-- se nao tiver single number, reportar null

SELECT MAX(num) AS num
FROM (
  SELECT num
  FROM MyNumbers
  GROUP BY num
  HAVING COUNT(*) = 1
);