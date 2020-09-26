from unittest import TestCase

from models import base
from api.models.digital_documents import *


class TestBase(TestCase):

    def setUp(self):
        pass

    def test_find_model_1(self):
        model = base.find_model('books')
        self.assertIsNotNone(model)

    def test_find_model_2(self):
        model = base.find_model('foo')
        self.assertIsNone(model)

    def test_to_json(self):
        pass
    
    def test_to_document(self):
        pass

    def test_set_from_document(self):
        pass

    def test_set_property(self):
        pass