# Write your MySQL query statement below
WITH retakeExams AS (
    SELECT student_id, subject, MIN(exam_date) AS first_exam, MAX(exam_date) AS last_exam
    FROM Scores
    GROUP BY student_id, subject
    HAVING COUNT(exam_date) >= 2
)
SELECT R.student_id, R.subject, S1.score AS first_score, S2.score AS latest_score 
FROM retakeExams R
JOIN Scores S1 ON 
    R.student_id = S1.student_id 
    AND R.subject = S1.subject
    AND R.first_exam = S1.exam_date
JOIN Scores S2 ON 
    R.student_id = S2.student_id 
    AND R.subject = S2.subject
    AND R.last_exam = S2.exam_date
WHERE S1.score < S2.score
ORDER BY R.student_id, R.subject;