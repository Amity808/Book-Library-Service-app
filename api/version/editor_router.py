from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.version import oauth
from db.database import get_db
from schemas.bookstore import EditorialBase
from api.repo.editiorial_repo import update_editors, create_editorial, list_all_editors, get_editorial_byid, delete_editorial_byid


router = APIRouter()


@router.post("/create-editor")
def create_editor(editor: EditorialBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    editors = create_editorial(editor, db)
    return editors


@router.get('/get-all-editor')
def get_editor(db: Session = Depends(get_db)):
    editors = list_all_editors(db)
    return editors


@router.put("/update-bk-editor")
def update_editor(id: int, editor: EditorialBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    editors = update_editors(id, editor, db)
    return {"Details": "Successfully updated"}


@router.get('/get-editorial/{id}')
def get_condition_by_id(id: int, db: Session = Depends(get_db)):
    edit = get_editorial_byid(id, db)
    return edit


@router.delete('/delete/{id}')
def deleted_editorial(id: int, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    del_edit = delete_editorial_byid(id, db)
    return del_edit
