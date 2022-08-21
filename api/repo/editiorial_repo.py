from fastapi import HTTPException, status
from sqlalchemy.orm import Session


from schemas.bookstore import EditorialBase
from models.user import Editorial


def create_editorial(editor: EditorialBase, db: Session):
    editors = Editorial(**editor.dict())
    db.add(editors)
    db.commit()
    db.refresh(editors)
    return editors


def list_all_editors(db: Session):
    editors = db.query(Editorial). all()
    return editors


def update_editors(id: int, editor: EditorialBase, db: Session):
    existing_editor = db.query(Editorial).filter(Editorial.id == id)
    if not existing_editor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Editorial not in register yet")
    editor.__dict__.update(id=id)
    existing_editor.update(editor.__dict__)
    db.commit()
    return existing_editor


def get_editorial_byid(id: int, db: Session):
    edit = db.query(Editorial).filter(Editorial.id == id).first()
    if not edit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Editorial does not exist")
    return edit


def delete_editorial_byid(id: int, db: Session):
    existing_editorial = db.query(Editorial).filter(Editorial.id == id)
    if not existing_editorial.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Editorial does not exist")
    existing_editorial.delete(synchronize_session=False)
    db.commit()
    return {"details": "Editorial successfully deleted"}

