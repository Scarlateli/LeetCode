SELECT
  ROUND(
    SUM(CASE WHEN a.order_date = a.customer_pref_delivery_date THEN 1 ELSE 0 END)
    / COUNT(*) * 100,
    2
  ) AS immediate_percentage
FROM delivery a
JOIN (
  SELECT customer_id, MIN(order_date) AS order_date
  FROM delivery
  GROUP BY customer_id
) b
  ON a.customer_id = b.customer_id
 AND a.order_date  = b.order_date;