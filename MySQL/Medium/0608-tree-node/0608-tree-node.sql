# Write your MySQL query statement below

SELECT id, 'Root' AS type
FROM Tree T1
WHERE T1.p_id IS NULL

UNION 

SELECT T2.id, 'Inner' AS type
FROM Tree T2
WHERE T2.p_id IS NOT NULL 
    AND T2.id IN (SELECT DISTINCT T.p_id FROM Tree T) 

UNION

SELECT T3.id, 'Leaf' AS type
FROM Tree T3
WHERE T3.p_id IS NOT NULL 
    AND NOT EXISTS (SELECT DISTINCT T.p_id FROM Tree T WHERE T3.id = T.p_id) 
