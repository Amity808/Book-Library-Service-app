from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.version import oauth
from db.database import get_db
from schemas.bookstore import GenreBase
from api.repo.genre_repo import create_genre, list_all_genre, update_genre, get_genre_byid, delete_genre_byid

router = APIRouter()


@router.post("/select_genre")
def select_genre(genre: GenreBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    genres = create_genre(genre, db)
    return genres


@router.get('/get-all-genre')
def get_genres(db: Session = Depends(get_db)):
    genres = list_all_genre(db)
    return genres


@router.put("/update-bk-genre")
def update_genre(id: int, genre: GenreBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    genres = update_genre(id, genre, db)
    return {"Details": "Successfully updated"}


@router.get('/get-genre/{id}')
def get_genre_by_id(id: int, db: Session = Depends(get_db)):
    gen = get_genre_byid(id, db)
    return gen


@router.delete('/delete/{id}')
def deleted_genre(id: int, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    del_gen = delete_genre_byid(id, db)
    return del_gen
