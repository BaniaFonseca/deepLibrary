import abc


class CRUD(abc.ABC):

    @abc.abstractmethod
    def get_one(self, modelclass, criteria):
        """Get a single document from the database and Return an instance 
        of the given Model class with its properties set with data of the matching document, 
        or ``None`` if no matching document is found

        :Parameters:

          - `modelclass`: a Model class that is a subclass of ``ModelABC`` 
            ex.: ``Book``

            >>> class ElectronicDocument(ModelABC): 
            >>> class Book(ElectronicDocument):
            
          - `criteria` : a document especifying the query criteria ex.: ``{'year': 2015}``.
        """

    @abc.abstractmethod
    def insert_one(self, model):
        """Insert the data provided by the model into the database 
        
        Return an ObjectId on success or ``None`` in failure

        :Parameters:

          - `model`: an object, the object must instance of a ``Model class``(ex.: Book) 
        """
