# Write your MySQL query statement below
SELECT user_id, email
FROM Users
WHERE REGEXP_LIKE(email, '^[a-zA-Z0-9_]+@[a-zA_Z]+\\.com$', 'c')
GROUP BY user_id
ORDER BY user_id;