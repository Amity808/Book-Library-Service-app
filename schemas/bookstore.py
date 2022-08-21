from datetime import datetime, date

from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    date_collected: Optional[date] = datetime.now().date()
    stock: int


class BookBorrowBase(BaseModel):
    date_borrow: Optional[date] = datetime.now().date()
    date_return: date = datetime.now().date()
    id_no: Optional[str] = None


class AuthorBase(BaseModel):
    firstname: str
    surname: str


class EditorialBase(BaseModel):
    press_name: str
    address: str


class GenreBase(BaseModel):
    type: str


class ConditionBase(BaseModel):
    name: Optional[str] = None
