import abc

class CRUD(abc.ABC):

    @abc.abstractmethod
    def get_object(self, bucketname, objectname):
        """Get a single object from the object storage

        :Parameters:

          - `bucketname`: The name of the bucket
          - `objerectname` : The name of the object
        """

    @abc.abstractmethod
    def save_object(self, bucketname, objectname, data, length, content_type):
        """Save a single object in the object storage

        :Parameters:

          - `bucketname`: The name of the bucket
          - `object` : The name of the object          
          - `data`: The data to be stored
          - `length` : The size of the data 
          - `contenttype` : Content type of the object.
        """
    