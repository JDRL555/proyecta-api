from enum import Enum
from datetime import date
from sqlmodel import SQLModel, Field
from typing import Optional

# Project complements
class ProjectType(str, Enum):
  PERSONAL: str = "personal"
  PROFESIONAL: str = "professional"

class ProjectCategory(SQLModel, table=True):
  __tablename__: str = "project_categories"
  
  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True, nullable=False, unique=True)
  description: Optional[str] = Field(index=True, nullable=True)
  
class ProjectCompanies(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True, nullable=False, unique=True)
  description: Optional[str] = Field(index=True, nullable=True)
  
# Main table
class Project(SQLModel, table=True):
  __tablename__: str = "projects"
  
  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True, nullable=False)
  type: ProjectType = Field(index=True, default=ProjectType.PERSONAL, nullable=False)
  company_id: int = Field(index=True, nullable=False)
  deadline: date = Field(index=True, default=date.today(), nullable=False)
  
  description: Optional[str] = Field(index=True, nullable=True)
  
  category_id: int = Field(foreign_key="project_categories.id", nullable=False)
  author_id: int = Field(foreign_key="users.id", nullable=False)
  
# Collaborators table
class ProjectCollabs(SQLModel, table=True):
  __tablename__: str = "project_collabs"
  
  id: int = Field(default=None, primary_key=True)
  project_id: int = Field(foreign_key="projects.id", nullable=False)
  collab_id: int = Field(foreign_key="users.id", nullable=False)