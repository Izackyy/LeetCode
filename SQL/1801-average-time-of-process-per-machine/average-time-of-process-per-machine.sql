# Write your MySQL query statement below
WITH endProcess AS (
    SELECT *
    FROM Activity
    WHERE activity_type = "end"
),
totalTime AS (
    SELECT 
        A.machine_id,
        COUNT(DISTINCT A.process_id) AS process_count, 
        SUM(E.timestamp - A.timestamp) AS process_time
    FROM Activity A
    JOIN endProcess E ON 
        A.machine_id = E.machine_id AND
        A.process_id = E.process_id
    WHERE A.activity_type = 'start'
    GROUP BY A.machine_id
)
SELECT 
    machine_id, 
    ROUND((process_time / process_count), 3) AS processing_time
FROM totalTime 