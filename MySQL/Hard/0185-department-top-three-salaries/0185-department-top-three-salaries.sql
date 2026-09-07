# Write your MySQL query statement below
WITH top_3 AS (
    SELECT 
        d.name AS Department,
        salary AS Salary,
        e.name AS Employee,
        DENSE_RANK() OVER(PARTITION BY d.id ORDER BY salary DESC) AS drnk
        FROM Department d
        JOIN Employee e ON d.id = e.departmentID
)
SELECT Department, Employee, Salary
FROM top_3 t
WHERE drnk <= 3;
