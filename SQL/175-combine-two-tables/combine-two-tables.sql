# Write your MySQL query statement below
SELECT firstName, lastName, City, State
FROM Person P
LEFT OUTER JOIN Address A ON P.personId = A.personId
