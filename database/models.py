from typing import List, Optional

from pydantic import AnyUrl, EmailStr
from sqlmodel import Field, Relationship, SQLModel


class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    employees: List["User"] = Relationship(back_populates="company")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    image: Optional[AnyUrl] = None

    company_id: Optional[int] = Field(default=None, foreign_key="company.id")
    company: Optional[Company] = Relationship(back_populates="employees")
