# Write your MySQL query statement below
SELECT S1.score, COUNT(DISTINCT S2.score) AS 'rank'
FROM Scores S1, Scores S2
WHERE S1.score <= S2.score
GROUP BY S1.id, S1.score
ORDER BY S1.score DESC