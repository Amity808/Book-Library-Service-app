from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.user import Book, BookBorrow, Author, Editorial, Genre, Condition
from schemas.bookstore import BookBase


def book_creation(book: BookBase, db: Session):
    books = Book(**book.dict())
    db.add(books)
    db.commit()
    db.refresh(books)
    return books


def get_book_byId(id: int, db: Session):
    books = db.query(Book).filter(Book.id == id).first()
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book does not exist")
    return books


def get_all(db: Session):
    books = db.query(Book).all()
    return books


def update_book(id: int, book: BookBase, db: Session):
    existing_books = db.query(Book).filter(Book.id == id)
    if not existing_books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"Book does not exist"})
    book.__dict__.update(id=id)
    existing_books.update(book.__dict__)
    db.commit()
    return existing_books


def delete_book_byId(id: int, db: Session):
    existing_book = db.query(Book).filter(Book.id == id)
    if not existing_book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book does not exist")
    existing_book.delete(synchronize_session=False)
    db.commit()
    return {"details": "Book successfully deleted"}
