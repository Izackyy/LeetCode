# Write your MySQL query statement below
SELECT E1.name AS name
FROM Employee E1
WHERE (
    SELECT COUNT(E2.id)
    FROM Employee E2
    WHERE E1.id = E2.managerId) >= 5;

