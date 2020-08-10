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
