from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from src.config import db, responses
from src.controllers.user import UserController

res = responses.custom_response

controller = UserController()

router = APIRouter(
  prefix="/users",
  responses={
    404: res(None, "User not found.", 404, True),
    401: res(None, "You don't have access. Please sign in first.", 401, True),
    403: res(None, "You don't have enough permission.", 403, True),
  }
)

@router.get("/")
async def get_users(session: Session = Depends(db.get_session)):
  return controller.get_users(session)

@router.get("/{user_id}")
async def get_user(session: Session = Depends(db.get_session), user_id: int = None):
  return controller.get_user(session, user_id)