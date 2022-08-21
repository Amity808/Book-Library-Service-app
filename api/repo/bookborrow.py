from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.bookstore import BookBorrowBase
from models.user import BookBorrow


def create_bk_borrow(borrow: BookBorrowBase, db: Session):
    book_borrow = BookBorrow(**borrow.dict())
    db.add(book_borrow)
    db.commit()
    db.refresh(book_borrow)
    return book_borrow


def list_all(db: Session):
    borrowed = db.query(BookBorrow). all()
    return borrowed


def update_return(id: int, borrow: BookBorrowBase, db: Session):
    existing_borrow = db.query(BookBorrow).filter(BookBorrow.id == id)
    if not existing_borrow:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You haven't borrow book yet")
    borrow.__dict__.update(id=id)
    existing_borrow.update(borrow.__dict__)
    db.commit()
    return existing_borrow


def get_bkborrow_byid(id: int, db: Session):
    borrowed = db.query(BookBorrow).filter(BookBorrow.id == id).first()
    if not borrowed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book borrow does not exist")
    return borrowed


def delete_bkborrow_byid(id: int, db: Session):
    existing_bkborrw = db.query(BookBorrow).filter(BookBorrow.id == id)
    if not existing_bkborrw.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book does not exist")
    existing_bkborrw.delete(synchronize_session=False)
    db.commit()
    return {"details": "Book borrowed successfully deleted"}
