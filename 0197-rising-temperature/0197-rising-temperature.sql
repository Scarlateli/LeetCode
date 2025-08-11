SELECT w1.id
FROM weather w1
WHERE EXISTS (
  SELECT 1
  FROM weather w2
  WHERE w2.recordDate = w1.recordDate - 1
    AND w2.temperature < w1.temperature
);

