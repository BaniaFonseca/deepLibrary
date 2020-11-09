from storage import oscrudabc
from storage.connection import Connection
import io

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
    
    def get_object(self, bucketname, objectname):
        try:
            response =  self.connection.get_object(bucketname, objectname)
            data = response.read()
        finally:
            response.close()
            response.release_conn()
        return data
            
    def get_partial_object(self, bucket_name, object_name, offset, length):
        response = self.connection.get_partial_object(bucket_name, object_name, offset, length)
        data = response.read()
        response.close()
        response.release_conn()
        return data
    
    def put_object(self, bucketname, objectname, data, length, contenttype):
        self.connection.put_object(
            bucketname, 
            objectname,
            data,
            length,
            contenttype)
    
    def remove_objects(bucket_name, objects_iter):
        self.connection.remove_objects(bucket_name, objects_iter)

    def make_bucket(name):
        return self.connection.make_bucket(name)