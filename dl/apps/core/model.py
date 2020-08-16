import abc

class ModelABC(abc.ABC):
    """Abstract Model Class 

        Every model must follow the guide rules bellow.
        If they do not, well, do not google, if errors pops up:

        1. It must inherite from ``ModelABC`` and implement 
        its defined abstractmethods

        2. It must precede the name of its properties with double underscore 
            ex.: self.___id
            If you are not familiar with pyhton, double underscore
            make the property private.   
        
        3. It must define for each property, a getter and a setter function 
        of the the same name (ignoring the double underscore) decorated 
        with  ``@property`` 
            ex.:
            >>> @property # is the getter function for the property self.___id
            >>> def _id(self):
            >>>     return self.___id

            >>> @_id.setter # is the setter function for property self.___id
            >>> def _id(self, value):
            >>>     self.___id = value
        
        4. It must ensure that the name of its properties (ignoring the double underscore)
        match the fields defined on the database schema.
        
        ex.:
            Let the database schema represented  by the model be:

            +---------+---------------+
            | fields  | type          |  
            +---------|---------------|
            | title   | string        |
            | authors | list of dicts |
            +---------|---------------|

            The class properties' name must be: self.__title,  self.__authors

            The setters and getters must be:

            >>> @property
            >>> def authors(self):
            >>>     return self.__authors 
    
            >>> @authors.setter
            >>> def authors(self, authors):
            >>>    self.__authors = authors    

            >>> @property
            >>> def title(self):
            >>>     return self.__title 

            >>> @title.setter
            >>> def title(self, value):
            >>>     self.__title = value
            ....
    """

    def __init__(self):
        self._id = None

    @property
    def _id(self):
        """ The id of the document represented by the model"""
        return self.___id

    @_id.setter
    def _id(self, value):
        self.___id = value

    @abc.abstractmethod
    def collection():
        """Return the collection's name to which the document represented by the model belong to
        
        The collection's name must be a fullqualified name
        ex.:

        if in the database the collection's name is: edocument.book

        >>> @property
        >>> def collection(self):
        >>>     return "edocument.book"

        or if in the database the collection's name is just: user

        >>> @property
        >>> def collection(self):
        >>>     return "user"


        """
    
    def set_from_document(self, document):
        """Set model's properties with data from given document"""
        for documentkey in document.keys():
            for classproperty in self.__dict__.keys():
                if classproperty.__contains__(documentkey):
                    if isinstance(document[documentkey], list):
                        self.__dict__[classproperty] = document[documentkey].copy()
                    else:
                        self.__dict__[classproperty] = document[documentkey]
                    

    def as_document(self):
        """ Return the the model as a document or ```None``
        if the model properties are not setted yet
        """
        document = {}
        for classproperty in self.__dict__.keys():
            documentkey = classproperty.split("__")
            documentkey = documentkey[1]
            if self.__dict__[classproperty] is not None:
                if isinstance(self.__dict__[classproperty], list):
                    document.__setitem__(documentkey, self.__dict__[classproperty].copy())
                else:
                    document.__setitem__(documentkey, self.__dict__[classproperty])
                
        return document if len(document) > 0 else None