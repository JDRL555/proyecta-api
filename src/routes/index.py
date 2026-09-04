from fastapi import APIRouter
from .user import router as user_router

app_router = APIRouter(prefix="/api")

app_router.include_router(user_router)