SELECT writer, AVG(to_date(created_at, 'YYYY') - to_date(publication_year::text, 'YYYY'))/365.25
FROM books
GROUP BY writer