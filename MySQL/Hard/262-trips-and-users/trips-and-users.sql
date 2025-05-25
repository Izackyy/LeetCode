-- # Write your MySQL query statement below
WITH unbannedTrips AS (
    SELECT *
    FROM Trips T
    WHERE EXISTS (
        SELECT *
        FROM Users U
        WHERE T.client_id = U.users_id AND U.banned = 'No'

        INTERSECT

        SELECT *
        FROM Users U
        WHERE T.driver_id = U.users_id AND U.banned = 'No'        
    ) AND (request_at = '2013-10-01' OR request_at = '2013-10-02' OR request_at = '2013-10-03')
),
validCancel AS (
    SELECT COUNT(status) AS cancelCount, request_at
    FROM unbannedTrips UT
    WHERE status <> 'completed'
    GROUP BY request_at
    ORDER BY request_at
),
validTotal AS (
    SELECT COUNT(status) AS totalCount, request_at
    FROM unbannedTrips UT
    GROUP BY request_at
    ORDER BY request_at
)

SELECT VT.request_at AS 'Day', ROUND(IFNULL(VC.cancelCount, 0) / VT.totalCount, 2) AS 'Cancellation Rate'
FROM validTotal VT
LEFT OUTER JOIN validCancel VC USING (request_at)
GROUP BY VT.request_at
ORDER BY VT.request_at



