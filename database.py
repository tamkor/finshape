from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})
session_local = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
