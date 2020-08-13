import abc

class ModelABC(abc.ABC):


    def __init__(self):
        self.id = None

    @property
    def id(self):
        """ The document id"""
        return self.___id

    @id.setter
    def id(self, value):
        self.___id = value

    @abc.abstractmethod
    def collection():
        """ Return the collection name assotiated with the  model """

    @abc.abstractmethod
    def embendeds():
        """Return a list of Embeded Model classes if one of the following
        condition hold:
    
            1. the model has a property aggregating Embeded Models 
            ex.: 
                >>> @property
                >>> def authors(self):
                >>>    # a list of  instances of class Author(EmbendedModelABC)
                >>>    return self.__authors
            
            2. the model has a property composing an Embeded Model
                ex.: 
                >>> @property
                >>> def author(self):
                >>>    # an instance of class Author(EmbendedModelABC)
                >>>    return self.__author
             
            if the above condition hold the model must return a list of Embeded Models.
            ex.:
            >>> @property
            >>> def embendeds(self):
            >>>     return [Author]

            otherwise, return None
            """

    def set_from_document(self, document):
        for documentkey in document.keys():
            self.id = document['_id']
            for classproperty in self.__dict__.keys():
                if classproperty.__contains__(documentkey):
                    self.__dict__[classproperty] = document[documentkey]
                    if self.embendeds is not None:
                        for embended in self.embendeds:
                            if documentkey.__contains__(embended().embendeddocument):
                                if isinstance(self.__dict__[classproperty], list):
                                    for i, value in enumerate(self.__dict__[classproperty], 0):
                                        embendedmodel = embended()
                                        embendedmodel.set_from_document(value)
                                        self.__dict__[classproperty][i] =  embendedmodel
                                else:
                                    embendedmodel = embended()
                                    embendedmodel.set_from_document(self.__dict__[classproperty])
                                    self.__dict__[classproperty] = embendedmodel
                                break
                    
    def as_document(self):
        document = {}
        for classproperty in self.__dict__.keys():
            documentkey = classproperty.split("__")
            if len(documentkey) == 2:
                documentkey = documentkey[1]
                if self.__dict__[classproperty] is not None:
                    document.__setitem__(documentkey, self.__dict__[classproperty])
                if self.embendeds is not None:
                    for embended in self.embendeds:
                        if documentkey.__contains__(embended().embendeddocument):
                            if isinstance(self.__dict__[classproperty], list):
                                document[documentkey] = document[documentkey].copy()
                                for i, value in enumerate(self.__dict__[classproperty], 0):
                                    document[documentkey][i] =  self.__dict__[classproperty][i].as_document()
                            else:
                                if self.__dict__[classproperty] is not None:
                                    document[documentkey] =  self.__dict__[classproperty].as_document()
                            break
        return document

class EmbendedModelABC(abc.ABC):
    """Embended Model class    
        
        We define ``Embeded Model`` as a ``Model`` that its assotiated document 
        in a database collection is found embended into another document
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

