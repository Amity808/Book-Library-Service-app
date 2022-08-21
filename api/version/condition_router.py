from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.version import oauth
from db.database import get_db
from schemas.bookstore import ConditionBase
from api.repo.condition_repo import update_condition, borrow_condition, list_all_condition, get_condition_byid, delete_condition_byid


router = APIRouter()


@router.post("/borrow-conditior")
def create_editor(condition: ConditionBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    cond = borrow_condition(condition, db)
    return cond


@router.get('/get-all-conditor')
def get_conditons(db: Session = Depends(get_db)):
    cond = list_all_condition(db)
    return cond


@router.put("/update-bk-condition")
def update_conditions(id: int, condition: ConditionBase, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    cond = update_condition(id, condition, db)
    return {"Details": "Successfully updated"}


@router.get('/get-condition/{id}')
def get_condition_by_id(id: int, db: Session = Depends(get_db)):
    borrowed = get_condition_byid(id, db)
    return borrowed


@router.delete('/delete/{id}')
def deleted_condition(id: int, db: Session = Depends(get_db), current_user = Depends(oauth.get_current_user)):
    del_cond = delete_condition_byid(id, db)
    return del_cond
