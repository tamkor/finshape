WITH ADDITIONAL AS (
    SELECT writer, copy_number, ROW_NUMBER() OVER (
        PARTITION BY writer
        ORDER BY publication_year
    ) PublicationRank
    FROM books
)
SELECT writer, copy_number
FROM ADDITIONAL
WHERE PublicationRank = 3