from apps.core.model import ModelABC, EmbendedModelABC
import apps.deepshelf.models.edocument as edocument
from apps.core.database.crud import CRUD


## Warning:  crud must be tested  ....
class Test:

    def __init__(self):
        self.a = "ola"

    def test(self, criteria=None):
        crud = CRUD()
        # book1 = crud.get_one(edocument.Book, criteria)
        # print(book1.as_document())

        book = edocument.Book()
        book.title = "introduction to algorithms"
        
        authors = [
            edocument.Author(name="cormen h. thomas", description="computer scientist"),
            edocument.Author(name="thomas h. cormen", description="computer scientist") 
        ]

        book.authors = authors
        book.edition = 2
        book.language = "en"
        book.pages = 750
        book.year = 2018
        book.publisher = "John Wiley & Sons, Inc"
        book.isbn = "978-1-118-99687-5"
        book.preface = " ..."
        book.volume = 2
        book.country = "U.S"
        book.city = "New York"


        print("insert")
        print(book.as_document())
        print("inserting ...")
        crud.insert_one(book)


