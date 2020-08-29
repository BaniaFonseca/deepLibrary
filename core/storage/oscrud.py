from core.storage import oscrudabc
from core.storage.connection import Connection

class OSCRUD(oscrudabc.OSCRUD):
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
        return self.connection.get_object(bucketname, objectname)
    
    def save_object(self, bucketname, objectname, data, length, contenttype):
        self.connection.put_object(
            bucketname, 
            objectname,
            data,
            length,
            contenttype)
