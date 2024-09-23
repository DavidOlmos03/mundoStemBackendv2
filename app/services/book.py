from app.services.base import ServiceBase
from app.schemas.book import BookUpdate, BookCreate, BookBase
from typing import Generic, TypeVar, Any
from datetime import date
# from app.protocols.db.utils.model import BaseModel
from app.protocols.db.models.book import Book
from app.protocols.db.crud.book import CRUDBookProtocol

# crea la tabla en la base de datos???
class BookService(ServiceBase[Book,BookBase,BookUpdate,CRUDBookProtocol]):
    def create(self, *, obj_in: BookBase)->Book:
        obj = obj_in
        # print("Este es el objeto en cuestion(book):",type(obj))
        return super().create(obj_in=obj)
    

    '''
        Función creada por JuanDavidR
    '''
    def get_books_by_subject_topic(
        self,
        *, 
        subject: int = 0,
        topic: int = 0,
        payload: dict[str, Any] | None = None,
        order_by: str | None = None,
        date_range: dict[str, date] | None = None,
        values: tuple[str] | None = None
        )->list[Book | dict[str,Any]]:
        if self.observer is None:
            return
        return self.observer.get_books_by_subject_topic(
            payload=payload,
            subject=subject,
            topic=topic,
            order_by=order_by,
            date_range=date_range,
            values=values,
        )



book_svc = BookService()