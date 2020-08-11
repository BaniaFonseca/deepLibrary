from . import crudabc
from . connection import Connection
from pymongo import MongoClient
from .. model import ModelABC

class CRUD(crudabc.CRUD):

    def __init__(self):
        super().__init__()
        self.connection = Connection.get_connection()

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
    
    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        self.__connection = value