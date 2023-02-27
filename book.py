from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter()


@router.get('/')
def get_books(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    books = db.query(models.Book).filter(models.Book.title.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(books), 'books': books}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_book(payload: schemas.BookBaseSchema, db: Session = Depends(get_db)):
    new_book = models.Book(**payload.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"status": "success", "book": new_book}


@router.patch('/{book_id}')
def update_book(book_id: str, payload: schemas.BookBaseSchema, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == book_id)
    db_books = book_query.first()

    if not db_books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No book with this id: {book_id} found')
    update_data = payload.dict(exclude_unset=True)
    book_query.filter(models.Book.id == book_id).update(update_data, synchronize_session="False")
    db.commit()
    db.refresh(db_books)
    return {"status": "success", "book": db_books}


@router.get('/{book_id}')
def get_post(book_id: str, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No book with this id: {id} found")
    return {"status": "success", "book": book}


@router.delete('/{book_id}')
def delete_post(book_id: str, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == book_id)
    book = book_query.first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No book with this id: {id} found')
    book_query.delete(synchronize_session="False")
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
