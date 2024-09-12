from app.services.base import ServiceBase
from app.schemas.book import BookUpdate, BookCreate, BookBase
# from app.protocols.db.utils.model import BaseModel
from app.protocols.db.models.physics_books import physics_books
from app.protocols.db.crud.book import CRUDBookProtocol

# crea la tabla en la base de datos???
class BookService(ServiceBase[physics_books,BookBase,BookUpdate,CRUDBookProtocol]):
    def create(self, *, obj_in: BookBase)->physics_books:
        obj = obj_in
        # print("Este es el objeto en cuestion(book):",type(obj))
        return super().create(obj_in=obj)
    


book_svc = BookService()