from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.version import oauth
from db.database import get_db
from schemas.bookstore import AuthorBase
from api.repo.author_repo import create_author, list_all_author, update_author, get_author_byid, delete_author_byid

router = APIRouter()


@router.post("/create_author")
def author_create(author: AuthorBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    authors = create_author(author, db)
    return authors


@router.get('/get-all-author')
def get_authors(db: Session = Depends(get_db)):
    authorss = list_all_author(db)
    return authorss


@router.put("/update-bk-author")
def update_borrowed(id: int, author: AuthorBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    authors = update_author(id, author, db)
    return {"Details": "Successfully updated"}


@router.get('/get-author/{id}')
def get_author_by_id(id: int, db: Session = Depends(get_db)):
    authors = get_author_byid(id, db)
    return authors


@router.delete('/delete/{id}')
def deleted_author(id: int, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    del_author = delete_author_byid(id, db)
    return del_author
