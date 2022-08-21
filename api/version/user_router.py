from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from api.repo.user import create_user, retrieve_user_id
from schemas.users import UserBase, UserResponse

router = APIRouter()


@router.post("/", response_model=UserResponse)
def user_create(user: UserBase, db: Session = Depends(get_db)):
    user = create_user(user, db)
    return user


@router.get("/")
def get_user_by_id(id: int, db: Session=Depends(get_db)):
    user = retrieve_user_id(id, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user
