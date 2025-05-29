# Write your MySQL query statement below
WITH 2019_orders AS (
    SELECT buyer_id AS user_id, order_id
    FROM Orders
    WHERE YEAR(order_date) = 2019
)
SELECT U.user_id AS buyer_id, U.join_date, COUNT(O.order_id) AS orders_in_2019
FROM Users U
LEFT OUTER JOIN 2019_orders O USING (user_id)
GROUP BY U.user_id, U.join_date