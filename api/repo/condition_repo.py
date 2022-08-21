from fastapi import HTTPException, status
from sqlalchemy.orm import Session


from schemas.bookstore import ConditionBase
from models.user import Condition


def borrow_condition(condition: Condition, db: Session):
    cond = Condition(**condition.dict())
    db.add(cond)
    db.commit()
    db.refresh(cond)
    return cond


def list_all_condition(db: Session):
    cond = db.query(Condition). all()
    return cond


def update_condition(id: int, condition: ConditionBase, db: Session):
    existing_condition = db.query(Condition).filter(Condition.id == id)
    if not existing_condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You haven't borrow book yet")
    condition.__dict__.update(id=id)
    existing_condition.update(condition.__dict__)
    db.commit()
    return existing_condition


def get_condition_byid(id: int, db: Session):
    cond = db.query(Condition).filter(Condition.id == id).first()
    if not cond:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Condition does not exist")
    return cond


def delete_condition_byid(id: int, db: Session):
    existing_conditon = db.query(Condition).filter(Condition.id == id)
    if not existing_conditon.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Condition does not exist")
    existing_conditon.delete(synchronize_session=False)
    db.commit()
    return {"details": "Condition successfully deleted"}
