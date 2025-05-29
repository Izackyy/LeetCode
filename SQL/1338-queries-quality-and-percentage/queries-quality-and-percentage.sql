# Write your MySQL query statement below
WITH poorQuality AS (
    SELECT query_name, COUNT(*) AS poorCount
    FROM Queries
    WHERE rating < 3
    GROUP BY query_name
),
indivQuality AS (
    SELECT query_name, (rating / position) AS indiv_quality
    FROM Queries
)
SELECT 
    I.query_name, 
    ROUND(AVG(indiv_quality), 2) AS quality, 
    ROUND((IF(poorCount IS NULL, 0, poorCount) / COUNT(I.query_name)) * 100, 2) AS poor_query_percentage
FROM indivQuality I
LEFT OUTER JOIN poorQuality P ON I.query_name = P.query_name
GROUP BY I.query_name 
