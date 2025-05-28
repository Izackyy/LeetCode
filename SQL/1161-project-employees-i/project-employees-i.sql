# Write your MySQL query statement below
WITH employeeCount AS (
    SELECT project_id, COUNT(employee_id) AS eCount
    FROM Project
    GROUP BY project_id
)
SELECT EC.project_id, ROUND((SUM(EM.experience_years) / EC.eCount), 2) AS average_years
FROM Employee EM
JOIN Project P ON EM.employee_id = P.employee_id
JOIN employeeCount EC ON P.project_id = EC.project_id 
GROUP BY EC.project_id
