/* Write your PL/SQL query statement below */
-- tabela sales 
-- achar todas as vendas que aconteceram no primeiro ano de vendas
-- para cada product_id, identifique o menor ano que aparece na tabela
-- retorne todas as vendas nesse ano 

-- retornar por product_id, first_year, quantity, and price.

SELECT
  s.product_id,
  m.first_year,
  s.quantity,
  s.price
FROM Sales s
JOIN (
  SELECT product_id, MIN(year) AS first_year
  FROM Sales
  GROUP BY product_id
) m
  ON s.product_id = m.product_id
 AND s.year = m.first_year;
