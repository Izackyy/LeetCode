# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers C
WHERE NOT EXISTS (SELECT id FROM Orders O WHERE C.id = O.customerId)