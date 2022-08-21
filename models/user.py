from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship

from .base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, nullable=False)
    date_of_birth = Column(Date)
    firstname = Column(String(50), nullable=False)
    second_name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    createDate = Column(Date, default=datetime.now)
    password = Column(String(50), nullable=False)
    card_id = Column(Integer, index=True)

    bookborrow = relationship("BookBorrow", back_populates='user')


class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    date_collected = Column(String)
    stock = Column(Integer)

    author_id = Column(Integer, ForeignKey('author.id'))
    editorial_id = Column(Integer, ForeignKey('editorial.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    condition_id = Column(Integer, ForeignKey('condition.id'))
    author = relationship("Author", back_populates='book')
    editorial = relationship("Editorial", back_populates='book')
    genre = relationship("Genre", back_populates='book')
    condition = relationship("Condition", back_populates='book')
    bookborrow = relationship("BookBorrow", back_populates='book')


class BookBorrow(Base):
    id = Column(Integer, primary_key=True, index=True)
    date_borrow = Column(Date, default=datetime.now)
    date_return = Column(Date)
    id_no = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    book_id = Column(Integer, ForeignKey('book.id'))

    user = relationship("User", back_populates='bookborrow')
    book = relationship("Book", back_populates='bookborrow')


class Author(Base):
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(30))
    surname = Column(String(30))
    book = relationship("Book", back_populates='author')


class Editorial(Base):
    id = Column(Integer, primary_key=True, index=True)
    press_name = Column(String(40), nullable=False)
    address = Column(String(50))
    book = relationship("Book", back_populates='editorial')


class Genre(Base):
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(30))
    book = relationship("Book", back_populates='genre')


class Condition(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    book = relationship("Book", back_populates='condition')
