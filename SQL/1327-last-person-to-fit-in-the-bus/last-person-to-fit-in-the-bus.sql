# Write your MySQL query statement below
WITH weightSum AS (
    SELECT *, SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
)
SELECT person_name
FROM weightSum
WHERE total_weight = (
    SELECT MAX(total_weight)
    FROM weightSum
    WHERE total_weight <= 1000
);