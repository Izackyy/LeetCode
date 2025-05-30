# Write your MySQL query statement below
WITH totalDistance AS (
    SELECT user_id, SUM(distance) AS total_distance
    FROM Rides
    GROUP BY user_id
)
SELECT name, COALESCE(total_distance, 0) AS travelled_distance
FROM Users U
LEFT OUTER JOIN totalDistance T ON U.id = T.user_id
ORDER BY total_distance DESC, name ASC;