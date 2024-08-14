from app.services.base import ServiceBase
from app.schemas.book import BookUpdate, BookCreate, BookCreateInDB
from app.protocols.db.utils.model import BaseModel
from app.protocols.db.models.book import Book
from app.protocols.db.crud.book import CRUDBookProtocol


class BookService(ServiceBase[Book,BookCreateInDB,BookUpdate,CRUDBookProtocol]):
    def create(serf, *, obj_in: BookCreate)->Book:
        obj = BookCreateInDB()
        return super().create(obj_in=obj)
    


book_svc = BookService()