/*SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
FETCH FIRST 1 ROWS ONLY;*/


SELECT customer_number
FROM (
  SELECT customer_number, COUNT(*) AS cnt
  FROM Orders
  GROUP BY customer_number
  ORDER BY cnt DESC
)
WHERE ROWNUM = 1;
