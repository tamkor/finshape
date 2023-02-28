from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter()


@router.get('/')
def get_books(attribute_name: str = '', attribute_value: str = '', db: Session = Depends(get_db)):
    if attribute_name and attribute_value and attribute_name in dir(models.Book):
        book_attr = getattr(models.Book, attribute_name)
        books = db.query(models.Book).filter(book_attr.contains(attribute_value)).all()
    else:
        books = db.query(models.Book).all()
    return books


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_book(payload: schemas.BookBaseSchema, db: Session = Depends(get_db)):
    new_book = models.Book(**payload.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.put('/{book_id}')
def update_book(book_id: str, payload: schemas.BookBaseSchema, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == book_id)
    db_books = book_query.first()

    if not db_books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No book with this id: {book_id} found')
    update_data = payload.dict(exclude_unset=True)
    book_query.update(update_data)
    db.commit()
    db.refresh(db_books)
    return db_books


@router.get('/{book_id}')
def get_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No book with this id: {id} found")
    return book


@router.delete('/{book_id}')
def delete_post(book_id: str, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == book_id)
    book = book_query.first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No book with this id: {id} found')
    book_query.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
