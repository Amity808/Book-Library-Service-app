from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator


SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

