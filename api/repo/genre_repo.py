from fastapi import HTTPException, status
from sqlalchemy.orm import Session


from schemas.bookstore import GenreBase
from models.user import Genre


def create_genre(genre: GenreBase, db: Session):
    genres = Genre(**genre.dict())
    db.add(genres)
    db.commit()
    db.refresh(genres)
    return genres


def list_all_genre(db: Session):
    genres = db.query(Genre). all()
    return genres


def update_genre(id: int, genre: GenreBase, db: Session):
    existing_genre = db.query(Genre).filter(Genre.id == id)
    if not existing_genre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not in register yet")
    genre.__dict__.update(id=id)
    existing_genre.update(genre.__dict__)
    db.commit()
    return existing_genre


def get_genre_byid(id: int, db: Session):
    gen = db.query(Genre).filter(Genre.id == id).first()
    if not gen:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre does not exist")
    return gen


def delete_genre_byid(id: int, db: Session):
    existing_gen = db.query(Genre).filter(Genre.id == id)
    if not existing_gen.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre does not exist")
    existing_gen.delete(synchronize_session=False)
    db.commit()
    return {"details": "Genre successfully deleted"}

