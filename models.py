from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP
from sqlalchemy.sql import func

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    title = Column(String)
    writer = Column(String)
    publisher = Column(String)
    publication_year = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    copy_number = Column(Integer)
