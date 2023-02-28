SELECT writer, AVG(created_at - julianday(publication_year))
FROM books
GROUP BY writer