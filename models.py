from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    writer = Column(String)
    publisher = Column(String)
    publication_year = Column(Integer)
    created_at = Column(String, default=func.now())
    copy_number = Column(Integer)
