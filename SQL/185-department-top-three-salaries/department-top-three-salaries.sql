# Write your MySQL query statement below
WITH salaryOrdered AS (
    SELECT DISTINCT salary, departmentId AS dID
    FROM Employee
    ORDER BY salary DESC
),

departmentTop3 AS (
    SELECT S1.salary, S1.dID
    FROM salaryOrdered S1
    WHERE (
        SELECT COUNT(*)
        FROM salaryOrdered S2
        WHERE S2.salary > S1.salary AND S1.dID = S2.dID
    ) < 3
)

SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Employee E
JOIN Department D ON E.departmentId = D.id
WHERE salary IN (
    SELECT salary
    FROM departmentTop3
    WHERE E.departmentId = dID
    );
