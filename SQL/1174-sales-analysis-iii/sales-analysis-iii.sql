# Write your MySQL query statement below
SELECT DISTINCT P.product_id, P.product_name
FROM Product P
JOIN Sales S1 ON P.product_id = S1.product_id
WHERE NOT EXISTS (
    SELECT *
    FROM Sales S2
    WHERE P.product_id = S2.product_id
        AND (S2.sale_date > '2019-03-31' OR S2.sale_date < '2019-01-01')
);
