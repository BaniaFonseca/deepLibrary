from storage import oscrudabc
from storage.connection import Connection

class OSCRUD(oscrudabc.AbstractCRUD):
    """ Object Storage CRUD Class"""
    def __init__(self):
        super().__init__()
        self.connection = Connection.get_connection()
    
    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        self.__connection = value
    
    def get_one(self, bucketname, objectname):
        return self.connection.get_object(bucketname, objectname)
    
    def put_object(self, bucketname, objectname, data, length, contenttype):
        self.connection.put_object(
            bucketname, 
            objectname,
            data,
            length,
            contenttype)
    
    def remove_objects(bucket_name, objects_iter):
        self.connection.remove_objects(bucket_name, objects_iter)
