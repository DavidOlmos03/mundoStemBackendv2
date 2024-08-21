from fastapi import APIRouter, HTTPException
from app.schemas.book import BookBase,BookCreate, BookUpdate,BookInDB
from app.services.book import book_svc

router = APIRouter()

# Crea un libro
@router.post("", response_model=BookInDB, status_code=201)
def create_book(*, new_book: BookBase) -> BookInDB:
    book = book_svc.create(obj_in=new_book)
    return book



@router.get("", response_model=list[BookInDB], status_code=200)
def get_all_book(*, skip: int = 0, limit: int = 10) -> list[BookInDB]:
    return book_svc.get_multi(skip=skip, limit=limit)


@router.get("/{id}", response_model=BookInDB, status_code=200)
def get_book(*, id: int) -> BookInDB:
    book = book_svc.get(id=id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book


@router.patch("/{id}", response_model=None)
def update_book(*, obj_in: BookUpdate, id: int) -> None:
    book = book_svc.get(id=id)
    if not book:
        raise HTTPException(404, "Book not found")
    book_svc.update(id=id, obj_in=obj_in)
    return None


@router.delete("/{id}", response_model=None, status_code=204)
def delete_book(*, id: int) -> None:
    book = book_svc.delete(id=id)
    if book == 0:
        raise HTTPException(404, "Book not found")
    return None
