from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.sql import func

from database.config import Base


class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    writer = Column(String)
    publisher = Column(String)
    publication_year = Column(Integer)
    created_at = Column(String, default=func.now())
    copy_number = Column(Integer)


class StatsModel(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    calculated_at = Column(String, default=func.now())

    sql_books_count_per_writer = Column(String)
    sql_book_counter_per_publisher = Column(String)
    sql_avg_book_age = Column(String)
    sql_youngest_and_oldest_book = Column(String)
    sql_distinct_books_until_specific_year = Column(String)
    sql_avg_archive_year_by_writer = Column(String)
    sql_copy_number_of_top_3_by_writer = Column(String)
