# Write your MySQL query statement below
WITH earliestYear AS (
SELECT product_id, MIN(year) AS first_year
FROM Sales
GROUP BY product_id
)
SELECT S.product_id, S.year AS first_year, S.quantity, S.price
FROM Sales S
JOIN earliestYear AS E 
    ON S.product_id = E.product_id
    AND S.year = E.first_year;
