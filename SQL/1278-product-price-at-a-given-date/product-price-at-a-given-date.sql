# Write your MySQL query statement below
SELECT product_id, new_price AS price
FROM Products P1
WHERE P1.change_date = (
    SELECT MAX(change_date) 
    FROM Products P2
    WHERE P1.product_id = P2.product_id
        AND P2.change_date <= '2019-08-16') 

UNION ALL

SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';