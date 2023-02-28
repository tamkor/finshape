import main
import requests as requests
from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.orm import Session

from database.config import get_db
from database.models import BookModel
from endpoints.stats import calculate_stats
from schemas.book_schema import BookBaseSchema

book_router = APIRouter()


@book_router.get('/')
def get_books(attribute_name: str = '', attribute_value: str = '', db: Session = Depends(get_db)):
    if attribute_name and attribute_value and attribute_name in dir(BookModel):
        book_attr = getattr(BookModel, attribute_name)
        books = db.query(BookModel).filter(book_attr.contains(attribute_value)).all()
    else:
        books = db.query(BookModel).all()
    return books


@book_router.post('/', status_code=status.HTTP_201_CREATED)
def create_book(payload: BookBaseSchema, db: Session = Depends(get_db)):
    new_book = BookModel(**payload.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    requests.put(f'http://{main.HOST}:{main.PORT}{main.routes["stats"]}')
    return new_book


@book_router.put('/{book_id}')
def update_book(book_id: str, payload: BookBaseSchema, db: Session = Depends(get_db)):
    book_query = db.query(BookModel).filter(BookModel.id == book_id)
    db_books = book_query.first()

    if not db_books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No book with this id: {book_id} found')
    update_data = payload.dict(exclude_unset=True)
    book_query.update(update_data)
    db.commit()
    db.refresh(db_books)
    requests.put(f'http://{main.HOST}:{main.PORT}{main.routes["stats"]}')
    return db_books


@book_router.get('/{book_id}')
def get_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No book with this id: {id} found")
    return book


@book_router.delete('/{book_id}')
def delete_book(book_id: str, db: Session = Depends(get_db)):
    book_query = db.query(BookModel).filter(BookModel.id == book_id)
    book = book_query.first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No book with this id: {id} found')
    book_query.delete()
    db.commit()
    requests.put(f'http://{main.HOST}:{main.PORT}{main.routes["stats"]}')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
