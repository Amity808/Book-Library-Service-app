from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import FastAPI
from sqlalchemy.orm import Session
from db.database import get_db
from api.repo.bookstore import book_creation, get_book_byId, get_all, update_book, delete_book_byId
from models.user import Book
from schemas.bookstore import BookBase
from . import oauth

router = APIRouter()


@router.post('/')
def create_book(book: BookBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    books = book_creation(book, db)
    return books


@router.get('/get-book/{id}')
def getbook_by_id(id: int, db: Session = Depends(get_db)):
    books = get_book_byId(id, db)
    return books


@router.get('/all-book')
def get_all_book(db: Session = Depends(get_db)):
    books = get_all(db)
    return books


@router.put('/update-book/{id}')
def update_book_id(id: int, book: BookBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    books = update_book(id, book, db)
    return {"details": "Book sucessfully Updated"}


@router.delete('/delete/{id}')
def deleted_book(id: int, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    del_book = delete_book_byId(id, db)
    return del_book
