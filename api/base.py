from fastapi import APIRouter
from .version import user_router, bookstore_router, router_borrow, router_author, editor_router, genre_router, \
    condition_router, authentication

api_router = APIRouter()

api_router.include_router(authentication.router, prefix="/login", tags=["Authentication"])
api_router.include_router(user_router.router, prefix="/user", tags=["Users"])
api_router.include_router(bookstore_router.router, prefix="/Library", tags=["Library"])
api_router.include_router(router_borrow.router, prefix="/Borrowbook", tags=["Library"])
api_router.include_router(router_author.router, prefix="/author", tags=["Library"])
api_router.include_router(editor_router.router, prefix="/editor", tags=["Library"])
api_router.include_router(genre_router.router, prefix="/genre", tags=["Library"])
api_router.include_router(condition_router.router, prefix="/condition", tags=["Library"])
