SELECT writer, publication_year, COUNT(id)
FROM books
GROUP BY writer, publication_year