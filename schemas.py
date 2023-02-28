from datetime import datetime
from pydantic.main import BaseModel


class BookBaseSchema(BaseModel):
    id: int | None = None
    title: str
    writer: str
    publisher: str
    publication_year: int
    created_at: str | None = None
    copy_number: int

    class Config:
        orm_mode = True
