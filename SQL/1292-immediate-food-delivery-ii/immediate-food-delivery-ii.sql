# Write your MySQL query statement below
WITH firstOrder AS (
    SELECT customer_id, MIN(order_date) AS firstDate
    FROM Delivery
    GROUP BY customer_id
),
immediateDelivery AS (
    SELECT D.customer_id
    FROM Delivery D
    JOIN firstOrder F ON D.customer_id = F.customer_id
    WHERE D.customer_pref_delivery_date = F.firstDate
)
SELECT ROUND((COUNT(DISTINCT I.customer_id) / COUNT(DISTINCT F.customer_id)) * 100, 2) AS immediate_percentage
FROM firstOrder F 
LEFT OUTER JOIN immediateDelivery I ON F.customer_id = I.customer_id
