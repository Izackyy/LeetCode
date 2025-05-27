# Write your MySQL query statement below
WITH unique2015 AS (
    SELECT tiv_2015
    FROM Insurance 
    GROUP BY tiv_2015
    HAVING COUNT(*) = 1
)

SELECT ROUND(SUM(I1.tiv_2016), 2) AS tiv_2016
FROM Insurance I1
WHERE NOT EXISTS (
    SELECT *
    FROM Insurance I2, unique2015 U
    WHERE I1.lat = I2.lat AND I1.lon = I2.lon AND I1.pid <> I2.pid
) 
AND I1.tiv_2015 NOT IN (SELECT * FROM unique2015);



-- SELECT ROUND(SUM(I1.tiv_2016), 2) AS tiv_2016
-- FROM Insurance I1
