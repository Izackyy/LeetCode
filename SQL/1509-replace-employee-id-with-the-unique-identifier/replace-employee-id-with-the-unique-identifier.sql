# Write your MySQL query statement below
SELECT unique_id, name
FROM EmployeeUNI U
RIGHT OUTER JOIN Employees E ON U.id = E.id 