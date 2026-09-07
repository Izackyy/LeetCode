# Write your MySQL query statement below
WITH pairCount AS (
    SELECT a.product_id AS product1_id, b.product_id AS product2_id, COUNT(b.product_id) AS customer_count
    FROM ProductPurchases a
    JOIN ProductPurchases b ON a.user_id = b.user_id AND a.product_id < b.product_id
    GROUP BY product1_id, product2_id
    HAVING customer_count >= 3  
) 
SELECT 
    product1_id, 
    product2_id, 
    b.category AS product1_category, 
    c.category AS product2_category,
    customer_count
FROM pairCount a
LEFT JOIN ProductInfo b ON a.product1_id = b.product_id
LEFT JOIN ProductInfo c ON a.product2_id = c.product_id
ORDER BY customer_count DESC, product1_id ASC, product2_id ASC;