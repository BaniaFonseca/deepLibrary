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
    
    def get_one(self, collection_name, criteria):
        model = base_model.find_model(collection_name)
        if model is not None:
            collection = self.connection[collection_name] 
            document = collection.find_one(criteria)
            if document is not None:
                model.set_from_document(document)
                return model
        return None

    def get_many(self, collection_name, criteria=None):
        models = []
        collection = self.connection[collection_name]    
        for doc in  collection.find(criteria):
            model = base_model.find_model(collection_name)
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
    
    def replace_one(self, model):
        document = model.to_document()
        if (len(document) > 0):
            collection = self.connection[model.collection]
            result = collection.replace_one({'_id': document['_id']}, document)
            return result.modified_count
        return None

    def update_one(self, collection_name, document, criteria=None):
        if (len(document) > 0):
            collection = self.connection[collection_name]
            result = collection.update_one(criteria, {"$set": document})
            return result.modified_count
        return None
    
    def delete_one(self, collection_name, criteria=None):
        collection = self.connection[collection_name]
        collection.delete_one(criteria)
        if collection.find(criteria) is None:
            return True
        else:
            return False
        