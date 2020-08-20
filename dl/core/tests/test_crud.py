from django.test import TestCase

from apps.core.model import ModelABC
import apps.deepshelf.models.edocument as edocument
from dl.core.database.crud import CRUD


class TestCRUD(TestCase):

    def setUp(self):
        pass

    def test_update_one(self):
        crud = CRUD()
        country = "UK"
        book = crud.get_one(edocument.Book, {'year': 2018})
        book.country = country
        crud.update_one(book)
        result = crud.get_one(edocument.Book, {'year': 2018})
        self.assertEqual(result.country, country)


    def bla(self, criteria=None):
        crud = CRUD()
        book1 = crud.get_one(edocument.Book, criteria)
        print(book1.as_document())

        book = edocument.Book()
        book.title = "introduction to algorithms"
        
        authors = [
            {'name' : 'cormen h. thomas', 'description' : 'computer scientist'},
            {'name' : 'thomas h. cormen', 'description' : 'computer scientist'} 
        ]

        book.authors = authors
        book.edition = 2
        book.language = "en"
        book.pages = 750
        book.year = 2020
        book.publisher = "John Wiley & Sons, Inc"
        book.isbn = "978-1-118-99687-5"
        book.preface = " ..."
        book.volume = 4
        book.country = "U.S"
        book.city = "New York"


        print("insert")
        print(book.as_document())
        
        print("inserting ...")
        crud.insert_one(book)


