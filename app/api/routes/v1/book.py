from fastapi import APIRouter, HTTPException
from app.schemas.book import BookBase,BookCreate, BookUpdate,BookInDB
from app.services.book import book_svc

router = APIRouter()

@router.post("", response_model=BookInDB, status_code=201)
def create_book(*, new_book: BookBase) -> BookInDB:
    book = book_svc.create(obj_in=new_book)
    return book