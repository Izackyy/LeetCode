# Write your MySQL query statement below
SELECT W2.id
FROM Weather W1, Weather W2
WHERE W2.recordDate = DATE_ADD(W1.recordDate, INTERVAL 1 DAY) 
    AND W1.temperature < W2.temperature;