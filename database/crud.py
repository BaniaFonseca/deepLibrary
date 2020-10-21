from bson.objectid import ObjectId
from pymongo import MongoClient

from database.crudabc import AbstractCRUD
from database.connection import Connection
from models import base_model

class CRUD(AbstractCRUD):

    def __init__(self):
        super().__init__()
        self.connection = Connection.get_connection()
    
    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        self.__connection = value
    
    def get_one(self, collection, criteria):
        model = base_model.find_model(collection)
        if model is not None:
            db_collection = self.connection[collection] 
            document = db_collection.find_one(criteria)
            if document is not None:
                model.set_from_document(document)
                return model
        return None

    def get_many(self, collection, criteria=None):
        models = []
        db_collection = self.connection[collection]    
        for doc in  db_collection.find(criteria):
            model = base_model.find_model(collection)
            model.set_from_document(doc)
            models.append(model)
        return models
        
    def insert_one(self, model):
        document = model.to_document()
        if (len(document) > 0):
            if document.__contains__('_id'):
                document.pop('_id')
            collection = self.connection[model.collection]
            result = collection.insert_one(document)
            return result.inserted_id
        return None
    
    def update_one(self, model):
        document = model.to_document()
        if (len(document) > 0):
            collection = self.connection[model.collection]
            result = collection.replace_one({'_id': document['_id']}, document)
            return result.modified_count
        return None