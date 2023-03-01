from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func

from db_access.config import Base


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
