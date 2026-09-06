# Write your MySQL query statement below
WITH allID AS (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
)
SELECT id, num
FROM (
    SELECT id, COUNT(id) AS num, RANK() OVER(ORDER BY COUNT(id) DESC) AS rank_ids
    FROM allID
    GROUP BY id
) as t
WHERE rank_ids = 1;