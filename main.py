from fastapi import FastAPI
from core.config import settings
from db.database import engine
from models.base_class import Base
from api.base import api_router


def create_table():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_table()
    include_router(app)
    return app


app = start_application()
