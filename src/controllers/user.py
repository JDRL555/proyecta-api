from fastapi import Depends
from sqlmodel import Session, select

from src.models.Users import User
from src.config import db, responses

res = responses.custom_response

class UserController:
  def get_users(self, session: Session = Depends(db.get_session)):
    users = session.exec(select(User)).all()
    
    return res(users)
  
  def get_user(self, session: Session = Depends(db.get_session), user_id: int = None):
    user = session.exec(select(User).where(User.id == user_id)).first()

    if not user:
      return res(None, "User not found.", 404)

    return res(user)