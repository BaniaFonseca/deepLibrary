from dl.settings.development import(
            DATABASE_NAME, 
            DATABASE_PASSWORD, 
            DATABASE_HOST, 
            DATABASE_PORT, 
            DATABASE_USER) 
from pymongo import MongoClient

class Connection:

    @staticmethod
    def get_connection():
        url = "mongodb://{}:{}@{}:{}/{}".format(
            DATABASE_NAME, 
            DATABASE_PASSWORD, 
            DATABASE_HOST, 
            DATABASE_PORT, 
            DATABASE_USER)
        connection = MongoClient(url) 
        return connection[DATABASE_NAME]         
