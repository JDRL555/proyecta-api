from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    __tablename__: str = "users"
  
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False, unique=True)
    password: str = Field(nullable=False)
    phone: Optional[str] = Field(index=True, nullable=True)