# Write your MySQL query statement below
WITH borrowedBooks AS (
    SELECT book_id, COUNT(book_id) AS borrow_count
    FROM borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
)
SELECT L.book_id, title, author, genre, publication_year, borrow_count AS current_borrowers
FROM library_books L
JOIN borrowedBooks B ON 
    L.book_id = B.book_id AND
    total_copies = borrow_count
ORDER BY current_borrowers DESC, title ASC;