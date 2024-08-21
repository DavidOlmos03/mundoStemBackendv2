from pydantic import BaseModel
from app.schemas.model import GeneralResponse
from typing import Optional

class BookBase(BaseModel):
    # id: Optional[int]
    title: str
    authors: str | None
    language: str | None
    subject: str | None
    pages: int | None
    extension: str | None
    size: int | None
    summary: str | None


class BookCreate(BaseModel):
    title: str
    authors: str | None
    language: str | None
    subject: str | None
    pages: int | None
    extension: str | None
    size: int | None
    summary: str | None


class BookUpdate(BaseModel):
    title: str
    authors: str | None
    language: str | None
    subject: str | None
    pages: int | None
    extension: str | None
    size: int | None
    summary: str | None

# class BookCreateInDB(BaseModel):
#     title: str
#     authors: str | None
#     language: str | None
#     subject: str | None
#     pages: int | None
#     extension: str | None
#     size: int | None
#     summary: str | None


class BookInDB(GeneralResponse, BookBase):
    ...