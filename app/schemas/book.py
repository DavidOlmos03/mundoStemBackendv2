from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    # id: Optional[int]
    title: str | None
    authors: str | None
    language: str | None
    subject: str | None
    pages: int | None
    extension: str | None
    size: int | None
    summary: str | None


class BookCreate(BookBase):
    title: str | None
    authors: str | None
    language: str | None
    subject: str | None
    pages: int | None
    extension: str | None
    size: int | None
    summary: str | None


class BookUpdate(BaseModel):
    title: str | None
    authors: str | None
    language: str | None
    subject: str | None
    pages: int | None
    extension: str | None
    size: int | None
    summary: str | None

class BookCreateInDB(BaseModel):
    title: str | None
    authors: str | None
    language: str | None
    subject: str | None
    pages: int | None
    extension: str | None
    size: int | None
    summary: str | None