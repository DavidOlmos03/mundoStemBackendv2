from fastapi import APIRouter, HTTPException
from app.schemas.book import BookCreate, BookUpdate, BookCreateInDB
from app.services.book import book_svc

router = APIRouter()

@router.post("", response_model=BookCreateInDB, status_code=201)
def create_book(*, new_book: BookCreate) -> BookCreateInDB:
    book = book_svc.create(obj_in=new_book)
    return book