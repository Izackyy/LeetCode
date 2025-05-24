# Write your MySQL query statement below

SELECT D.name AS Department, E.name AS Employee, salary AS Salary
FROM Employee E 
JOIN Department D ON E.departmentId = D.id
WHERE E.salary = 
    (SELECT MAX(salary)
    FROM Employee E2
    WHERE E.departmentId = E2.departmentId);