from bson.objectid import ObjectId

from apps.core.database import crudabc
from apps.core.database.connection import Connection
from pymongo import MongoClient
from apps.core.model import ModelABC

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
        if not issubclass(modelclass, ModelABC):
            "must throw an exception"
            print("The given modelclass is a a subclass of {}".format(modelclass))
            print("But modelclass must be a subclass of {}".format(ModelABC))
            return None
        model = modelclass()
        collection = self.connection[model.collection] 
        document = collection.find_one(criteria)
        if document is None:
            return None
        else:
            model.set_from_document(document)
            return model
   
    def insert_one(self, model):
        if not isinstance(model, ModelABC):
            "must throw an exception"
            print("The given model is an instance of {}".format(model))
            print("But model must be an instance of {}".format(ModelABC))
            return None
        document = model.as_document()
        if document.__contains__('_id'):
            document.pop('_id')
        collection = self.connection[model.collection] 
        result =  collection.insert_one(document)
        return result.inserted_id