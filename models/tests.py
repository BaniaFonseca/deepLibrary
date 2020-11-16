from unittest import TestCase
from bson.objectid import ObjectId

from models import base_model
from api.models.resources import *


class TestBase(TestCase):

    def setUp(self):
        self.document = { "_id" : ObjectId("5f390b30ea0e67ac51555b32"), 
                "title" : "introduction to algorithms", 
                "year" : 2020,
                "country" : "U.S", "city" : "New York", 
                "authors" : [ { "name" : "cormen h. thomas", "description" : "computer scientist" }, 
                { "name" : "thomas h. cormen", "description" : "computer scientist" } ], 
                "publisher" : "John Wiley & Sons, Inc", 
                "pages" : 750, 
                "preface" : " ...", 
                "isbn" : "978-1-118-99687-5", 
                "volume" : 4, 
                "edition" : 2, 
                "language" : "en", 
                "type" : "book" }

    def test_find_model_1(self):
        model = base_model.find_model('books')
        class_name = model.__class__.__name__
        self.assertEquals(class_name, 'Book')

    def test_find_model_2(self):
        model = base_model.find_model('foo')
        self.assertIsNone(model)

        
    def test_set_from_document_1(self):
        book = Book()
        book.set_from_document(self.document)
        expected = book.to_document()
        self.assertEquals(self.document, expected)

    def test_to_json(self):
        book = Book()
        book.set_from_document(self.document)
        expected = book.to_json()
        json = self.document.copy()
        json['id'] = str(json.pop('_id'))
        json['collection'] = book.collection
        self.assertEquals(json, expected)