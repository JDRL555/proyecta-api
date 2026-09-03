from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from src.config import db
from src.models.Users import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users(session: Session = Depends(db.get_session)):
    users = session.exec(select(User)).all()
    
    return {"users": users}