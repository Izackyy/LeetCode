# Write your MySQL query statement below
SELECT name, bonus
FROM Employee E
LEFT OUTER JOIN Bonus B USING (empId)
WHERE bonus < 1000 OR bonus IS NULL;
