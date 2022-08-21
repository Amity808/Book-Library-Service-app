from sqlalchemy.orm import Session
from schemas.users import UserBase, UserResponse
from models.user import User
from core.hashing import Haser


def create_user(user: UserBase, db: Session):
    users = User(
        email=user.email,
        date_of_birth=user.date_of_birth,
        surname=user.surname,
        firstname=user.firstname,
        second_name=user.second_name,
        address=user.address,
        password=Haser.bcrypt(user.password),
        card_id=user.card_id
    )
    db.add(users)
    db.commit()
    db.refresh(users)
    return users


def retrieve_user_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    return user
