from enum import Enum
from datetime import date
from sqlmodel import SQLModel, Field
from typing import Optional

class TaskStatus(str, Enum):
  PENDING: str = "pending"
  IN_PROGRESS: str = "in_progress"
  COMPLETED: str = "completed"
  CANCELED: str = "canceled"

class Task(SQLModel, table=True):
    __tablename__: str = "tasks"
  
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    description: Optional[str] = Field(index=True, nullable=True)
    start_date: date = Field(index=True, default=date.today(), nullable=False)
    end_date: Optional[date] = Field(index=True, nullable=True)
    status: TaskStatus = Field(index=True, default=TaskStatus.PENDING, nullable=False)
    project_id: int = Field(foreign_key="projects.id", nullable=False)
    assigned_to: int = Field(foreign_key="users.id", nullable=False)