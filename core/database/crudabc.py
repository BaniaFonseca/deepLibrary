import abc


class CRUD(abc.ABC):

    @abc.abstractmethod
    def get_one(self, modelclass, criteria):
        """Get single model, or ``None`` if no matching document is found

        :Parameters:

          - `modelclass`: a Model class that is a subclass of ``ModelABC`` 
            ex.: ``Book``

            >>> class ElectronicDocument(ModelABC): 
            >>> class Book(ElectronicDocument):
            
          - `criteria` : a document especifying the query criteria ex.: ``{'year': 2015}``.
        """

    @abc.abstractmethod
    def insert_one(self, model):
        """Insert single model 
        
        Return an ObjectId on success or ``None`` in failure

        :Parameters:

          - `model`: an object, the object must an instance of a ``Model class``(ex.: Book) 
        """

    @abc.abstractmethod
    def update_one(self, model):
        """Update single model    
        
        Return ``1`` on success or ``0`` otherwise 

        :Parameters:

          - `model`: an object, the object must an instance of a ``Model class``(ex.: Book) 
        """
