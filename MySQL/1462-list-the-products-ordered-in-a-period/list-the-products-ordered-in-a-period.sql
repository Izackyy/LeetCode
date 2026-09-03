# Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit
FROM Products P
JOIN Orders O ON P.product_id = O.product_id
WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'
GROUP BY P.product_id, product_name
HAVING SUM(unit) >= 100;