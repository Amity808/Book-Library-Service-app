from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from api.version import oauth
from db.database import get_db
from schemas.bookstore import BookBorrowBase
from api.repo.bookborrow import create_bk_borrow, list_all, update_return, get_bkborrow_byid, delete_bkborrow_byid


router = APIRouter()


@router.post('/borrow_book')
def borrow_book(borrow: BookBorrowBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    borrw_book = create_bk_borrow(borrow, db)
    return borrw_book


@router.get('/get-all-borrowed-book')
def get_all_bkborrow(db: Session = Depends(get_db)):
    borrwbook = list_all(db)
    return borrwbook


@router.put("/update-bk-book")
def update_borrowed(id: int, borrow: BookBorrowBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    borro_bk = update_return(id, borrow, db)
    return {"Details": "Successfully updated"}


@router.get('/get-bkborrow/{id}')
def get_bkborrow_by_id(id: int, db: Session = Depends(get_db)):
    borrowed = get_bkborrow_byid(id, db)
    return borrowed


@router.delete('/delete/{id}')
def deleted_bkborrow(id: int, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    del_borrowed = delete_bkborrow_byid(id, db)
    return del_borrowed
