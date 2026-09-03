-- # Write your MySQL query statement below
WITH sellingPrice AS (
    SELECT 
        P.product_id AS product_id, 
        price * IF(units IS NULL, 0, units) AS selling_price,
        IF(units IS NULL, 0, units) AS units
    FROM Prices P
    LEFT OUTER JOIN UnitsSold U ON 
        P.product_id = U.product_id AND
        purchase_date BETWEEN start_date AND end_date
)
SELECT 
    product_id, 
    ROUND(SUM(selling_price) / IF(SUM(units) = 0, 1, SUM(units)), 2) AS average_price
FROM sellingPrice 
GROUP BY product_id;
