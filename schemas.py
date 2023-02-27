from datetime import datetime
from typing import List

from pydantic.main import BaseModel


class BookBaseSchema(BaseModel):
    id: str | None = None
    title: str
    writer: str
    publisher: str
    publication_year: datetime
    created_at: datetime | None = None
    copy_number: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListBookResponse(BaseModel):
    status: str
    results: int
    books: List[BookBaseSchema]
