from sqlmodel import Field, SQLModel
from typing import Optional, List


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(SQLModel):
    username: str
    email: str
    password: str


class UserRead(SQLModel):
    id: int
    username: str
    email: str
    is_active: bool
    is_superuser: bool


class UserUpdate(SQLModel):
    username: str
    email: str
    password: str


class UserDelete(SQLModel):
    id: int


class UserLogin(SQLModel):
    username: str
    password: str


class UserToken(SQLModel):
    access_token: str
    token_type: str


class UserTokenData(SQLModel):
    username: Optional[str] = None
    scopes: List[str] = []
