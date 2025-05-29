# Write your MySQL query statement below
WITH allCombinations AS (
    SELECT *
    FROM Students, Subjects
)
SELECT 
    A.student_id AS student_id, 
    A.student_name AS student_name,
    A.subject_name AS subject_name,
    COUNT(E.student_id) AS attended_exams
FROM allCombinations A 
LEFT OUTER JOIN Examinations E ON (A.student_id = E.student_id AND A.subject_name = E.subject_name)
GROUP BY A.student_id, A.student_name, A.subject_name
ORDER BY A.student_id, A.subject_name;

