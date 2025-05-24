-- Write your PostgreSQL query statement below
DELETE FROM Person
WHERE id IN
    (SELECT P1.id
     FROM Person P1, Person P2 
     WHERE P1.id > P2.id AND P1.email = P2.email);