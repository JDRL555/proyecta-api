from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from src.config import db

from src.models.Users import User
from src.models.Projects import ProjectType, ProjectCategory, ProjectCompanies, Project, ProjectCollabs
from src.models.Task import TaskStatus, Task

from src.routes.index import app_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(app_router)