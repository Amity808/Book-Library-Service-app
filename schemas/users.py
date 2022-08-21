from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import datetime, date


class UserBase(BaseModel):
    email: EmailStr
    date_of_birth: date
    surname: str
    firstname: str
    second_name: str
    address: str
    password: str
    card_id: int


class UserResponse(BaseModel):
    email: str
    surname: str
    firstname: str
    second_name: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None