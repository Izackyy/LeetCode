# Write your MySQL query statement below
WITH userCount AS (
    SELECT user_id, COUNT(*) AS user_count
    FROM MovieRating
    GROUP BY user_id
), 
ratingSUM AS (
    SELECT movie_id, (SUM(rating) / COUNT(*)) AS average_rating
    FROM MovieRating
    WHERE DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
    GROUP BY movie_id
)
SELECT MIN(U.name) AS results
FROM Users U
JOIN userCount C ON U.user_id = C.user_id
WHERE user_count = (SELECT MAX(user_count) FROM userCount)

UNION ALL

SELECT MIN(title)
FROM Movies M
JOIN ratingSum R ON M.movie_id = R.movie_id
WHERE average_rating = (SELECT MAX(average_rating) FROM ratingSum);