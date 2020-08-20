from bson.objectid import ObjectId
from pymongo import MongoClient

from core.database import crudabc
from core.database.connection import Connection
from core.model import ModelABC
from core.exceptions import IsNotSubClassOfModelABC

class CRUD(crudabc.CRUD):

    def __init__(self):
        super().__init__()
        self.connection = Connection.get_connection()
    
    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        self.__connection = value
    
    def get_one(self, modelclass, criteria):
        model = modelclass()
        collection = self.connection[model.collection] 
        document = collection.find_one(criteria)
        if document is not None:
            model.set_from_document(document)
            return model
        return None
        
    def insert_one(self, model):
        document = model.as_document()
        if document.__contains__('_id'):
            document.pop('_id')
        collection = self.connection[model.collection]
        if (len(document) > 0): 
            result = collection.insert_one(document)
            return result.inserted_id
        return None
    
    def update_one(self, model):
        document = model.as_document()
        collection = self.connection[model.collection]
        result = collection.replace_one({'_id': document['_id']}, document)
        return result.modified_count
        