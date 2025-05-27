# Write your MySQL query statement below
WITH startDate AS (
SELECT player_id, MIN(event_date) AS startdate
FROM Activity
GROUP BY player_id),

validPlayers AS (
    SELECT COUNT(DISTINCT A.player_id) AS playerCount
    FROM Activity A
    JOIN startDate S ON A.player_id = S.player_id
    WHERE A.event_date = DATE_ADD(S.startdate, INTERVAL 1 DAY)
)

SELECT ROUND(V.playerCount / COUNT(DISTINCT A.player_id), 2) AS fraction
FROM Activity A, validPlayers V
