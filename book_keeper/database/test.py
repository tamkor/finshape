from sqlalchemy import text
from sqlalchemy import create_engine

SQLITE_DATABASE_URL = "sqlite:///./book_keeper.db"
engine = create_engine(SQLITE_DATABASE_URL, echo=True)

with engine.connect() as conn:
    result = conn.execute(text("""
    
        SELECT title
        FROM books
        WHERE publication_year = (SELECT MAX(publication_year) FROM books)

        UNION ALL

        SELECT title
        FROM books
        WHERE publication_year = (SELECT MIN(publication_year) FROM books)


    
    """))
    print(result.all())