SELECT title
FROM books
WHERE publication_year = (SELECT MAX(publication_year) FROM books)

UNION ALL

SELECT title
FROM books
WHERE publication_year = (SELECT MIN(publication_year) FROM books)