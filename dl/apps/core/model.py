import abc

class ModelABC(abc.ABC):


    def __init__(self):
        self.id = None

    @property
    def id(self):
        """ The id of the document represented by the model"""
        return self.___id

    @id.setter
    def id(self, value):
        self.___id = value

    @abc.abstractmethod
    def collection():
        """Return the database collection's name to which the document represented by the model belong to"""

    @abc.abstractmethod
    def embended_model_classes():
        """Return a list of `Embeded Model classes` or ``None`` if the model 
        do not contain any instance of any `Embeded Model Class`
        
        Usage:    
                If the model contains instance or instances of an `Embeded Model Class` 
                that `Embeded Model Class` must be included on the reurned list

                ex.: 
                    >>> class Book(ElectronicDocument):
                    >>>     # A Book class Model
                    >>>     def __init__(self):
                    >>>         self.authors = None
                    >>>     @property
                    >>>     def authors(self):
                    >>>         # A list of instances of class Author(EmbendedModelABC)
                    >>>         return self.__authors
                    >>>     @property
                    >>>     def embended_model_classes(self):
                    >>>         return [Author]
        """

    def set_from_document(self, document):
        """Set model's properties with data from given document"""
        for documentkey in document.keys():
            self.id = document['_id']
            for classproperty in self.__dict__.keys():
                if classproperty.__contains__(documentkey):
                    if isinstance(document[documentkey], list):
                        self.__dict__[classproperty] = document[documentkey].copy()
                    else:
                        self.__dict__[classproperty] = document[documentkey]
                    if self.embended_model_classes is not None:
                        for embendedmodelclass in self.embended_model_classes:
                            if documentkey.__contains__(embendedmodelclass().embendeddocument):
                                if isinstance(document[documentkey], list):
                                    for i, value in enumerate(document[documentkey], 0):
                                        embendedmodel = embendedmodelclass()
                                        embendedmodel.set_from_document(value)
                                        self.__dict__[classproperty][i] = embendedmodel
                                else:
                                    embendedmodel = embendedmodelclass()
                                    embendedmodel.set_from_document(document[documentkey])
                                    self.__dict__[classproperty] = embendedmodel
                                break
                    
                    
    def as_document(self):
        """ Return the the model as a document"""
        document = {}
        for classproperty in self.__dict__.keys():
            documentkey = classproperty.split("__")
            if len(documentkey) == 2:
                documentkey = documentkey[1]
                if self.__dict__[classproperty] is not None:
                    if isinstance(self.__dict__[classproperty], list):
                        document.__setitem__(documentkey, self.__dict__[classproperty].copy())
                    else:
                        document.__setitem__(documentkey, self.__dict__[classproperty])
                if self.embended_model_classes is not None:
                    for embendedmodelclass in self.embended_model_classes:
                        if documentkey.__contains__(embendedmodelclass().embendeddocument):
                            if isinstance(self.__dict__[classproperty], list):
                                for i, value in enumerate(self.__dict__[classproperty], 0):
                                    document[documentkey][i] = self.__dict__[classproperty][i].as_document()
                            else:
                                if self.__dict__[classproperty] is not None:
                                    document[documentkey] =  self.__dict__[classproperty].as_document()
                            break
        return document

class EmbendedModelABC(abc.ABC):
    """Embended Model class    
        
        We define ``Embeded Model`` as a ``Model`` that its assotiated document 
        in the database collection is found embended into another document
    """

    @abc.abstractmethod
    def embendeddocument():
        """Return the name of the embended document assotiated with the Embeded Model 
        
        ex.:
        for the document  { "authors" : [ { "firstname" : "Christopher", "surname" : " Negus" } ], "title" : "Linux Bible"}

        >>> def embendeddocument():
        >>>     return "author"

        embendeddocument must always be singular 
        """

    def set_from_document(self, document):
        for documentkey in document.keys():
            for classproperty in self.__dict__.keys():
                if classproperty.__contains__(documentkey):
                    self.__dict__[classproperty] = document[documentkey]
    
    
    def as_document(self):
        document = {}
        for classproperty in self.__dict__.keys():
            documentkey = classproperty.split("__")
            if len(documentkey) == 2:
                documentkey = documentkey[1]
                if self.__dict__[classproperty] is not None:    
                    document.__setitem__(documentkey, self.__dict__[classproperty])

        return document
