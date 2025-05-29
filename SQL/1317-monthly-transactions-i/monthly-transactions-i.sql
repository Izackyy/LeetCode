# Write your MySQL query statement below
WITH approvedTrans AS (
    SELECT 
        DATE_FORMAT(trans_date, '%Y-%m') AS month, 
        country, 
        COUNT(*) AS approved_count, 
        SUM(amount) AS approved_total_amount
    FROM Transactions
    WHERE state = 'approved'
    GROUP BY month, country
),
totalTrans AS (
    SELECT 
        DATE_FORMAT(trans_date, '%Y-%m') AS month, 
        country, 
        COUNT(*) AS trans_count, 
        SUM(amount) AS trans_total_amount
    FROM Transactions
    GROUP BY month, country
)
SELECT        
    T.month, 
    T.country, 
    trans_count, 
    IF(approved_count IS NULL, 0, approved_count) AS approved_count,
    trans_total_amount,
    IF(approved_total_amount IS NULL, 0, approved_total_amount) AS approved_total_amount
FROM totalTrans T
LEFT OUTER JOIN approvedTrans A ON (T.month <=> A.month AND T.country <=> A.country)


