from fastapi import HTTPException, status
from sqlalchemy.orm import Session


from schemas.bookstore import AuthorBase
from models.user import Author


def create_author(author: AuthorBase, db: Session):
    authors = Author(**author.dict())
    db.add(authors)
    db.commit()
    db.refresh(authors)
    return authors


def list_all_author(db: Session):
    author = db.query(Author). all()
    return author


def update_author(id: int, author: AuthorBase, db: Session):
    existing_author = db.query(Author).filter(Author.id == id)
    if not existing_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not in register yet")
    author.__dict__.update(id=id)
    existing_author.update(author.__dict__)
    db.commit()
    return existing_author


def get_author_byid(id: int, db: Session):
    authors = db.query(Author).filter(Author.id == id).first()
    if not authors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author does not exist")
    return authors


def delete_author_byid(id: int, db: Session):
    existing_author = db.query(Author).filter(Author.id == id)
    if not existing_author.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author does not exist")
    existing_author.delete(synchronize_session=False)
    db.commit()
    return {"details": "Author successfully deleted"}
