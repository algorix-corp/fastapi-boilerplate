from sqlmodel import Field, SQLModel
from typing import Optional, List


class Post(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = False
    author_id: int


class PostCreate(SQLModel):
    title: str
    content: str
    published: bool = False
    author_id: int


class PostRead(SQLModel):
    id: int
    title: str
    content: str
    published: bool
    author_id: int


class PostUpdate(SQLModel):
    title: str
    content: str
    published: bool


class PostDelete(SQLModel):
    id: int


class PostPublish(SQLModel):
    id: int
    published: bool = True


class PostUnpublish(SQLModel):
    id: int
    published: bool = False


class PostList(SQLModel):
    id: int
    title: str
    published: bool
    author_id: int
