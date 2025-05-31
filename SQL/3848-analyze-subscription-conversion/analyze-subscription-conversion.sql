# Write your MySQL query statement below
WITH freeTrial AS (
SELECT user_id, ROUND((SUM(activity_duration) / COUNT(activity_date)), 2) AS trial_avg_duration
FROM UserActivity
WHERE activity_type = 'free_trial'
GROUP BY user_id
),
paidPlan AS (
    SELECT user_id, ROUND((SUM(activity_duration) / COUNT(activity_date)), 2) AS paid_avg_duration
    FROM UserActivity
    WHERE activity_type = 'paid'
    GROUP BY user_id
)
SELECT P.user_id, trial_avg_duration, paid_avg_duration
FROM paidPlan P
JOIN freeTrial F ON P.user_id = F.user_id
ORDER BY P.user_id ASC;