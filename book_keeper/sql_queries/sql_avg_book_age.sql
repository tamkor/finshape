SELECT AVG(strftime('%Y', datetime('now')) - julianday(publication_year))
FROM books