SELECT publisher, COUNT(id)
FROM books
GROUP BY publisher