CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    SELECT DISTINCT salary
    FROM Employee E1
    WHERE N - 1 = (
        SELECT COUNT(DISTINCT salary)
        FROM Employee E2
        WHERE E2.salary > E1.salary AND E1.id <> E2.id
    )
  );
END