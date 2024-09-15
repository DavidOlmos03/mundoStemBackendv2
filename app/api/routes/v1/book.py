from fastapi import APIRouter, HTTPException
from app.schemas.book import BookBase,BookCreate, BookUpdate,BookInDB
from app.services.book import book_svc

"""
    Para hacer la consulta dado el nombre de la tabla
"""
from sqlalchemy import MetaData,Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
Base = declarative_base()

engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine) #ESTUDIAR
session = Session()
# from connection.connection import engine,Base, session

router = APIRouter()

# Crea un libro
@router.post("", response_model=BookInDB, status_code=201)
def create_book(*, new_book: BookBase) -> BookInDB:
    book = book_svc.create(obj_in=new_book)
    return book

# Obtener todos los libros
@router.get("", response_model=list[BookInDB], status_code=200)
def get_all_book(*, skip: int = 0, limit: int = 10) -> list[BookInDB]:
    return book_svc.get_multi(skip=skip, limit=limit)

# Obtener libros por id
@router.get("/{id}", response_model=BookInDB, status_code=200)
def get_book(*, id: int) -> BookInDB:
    book = book_svc.get(id=id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book

# Obtener los libros por subject (asignatura)
@router.get("/subject/{subject}", response_model=list[BookInDB], status_code=200)
def get_books_by_subject(subject: int) -> list[BookInDB]:
    return book_svc.get_books_by_subject(subject=subject)



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
