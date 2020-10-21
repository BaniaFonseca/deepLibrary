import abc 


class AbstractModel(abc.ABC):    
    """Abstract Model Class 

        Every model must follow the guide rules bellow.
        If they do not, well, do not google, if errors pops up:

        1. It must inherite from ``AbstractModel`` and implement 
        its defined abstractmethods

        2. It must precede the name of its properties with double underscore 
            ex.: self.___id
            If you are not familiar with pyhton, double underscore
            make the property private.   
        
        3. It must define for each property, a getter and a setter function 
        of the the same name (ignoring the double underscore) decorated 
        with  ``@property`` 
            ex.:
            >>> @property # is the getter function for the property self.__title
            >>> def title(self):
            >>>     return self.__title

            >>> @_id.setter # is the setter function for property self.__title
            >>> def title(self, value):
            >>>     self.___title = value
        
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
    """
    
    subclasses = {}

    def __init_subclass__(cls, is_abstract=False, **kwargs):
        super().__init_subclass__(**kwargs)
        if not is_abstract:
            cls.subclasses[cls().collection] = cls

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
    def collection(self):
        """Return the collection's name to which the document 
            represented by the model belong to
        """
        pass

    def set_from_document(self, document):
        doc = document.copy()
        """Set model's properties with data from given document"""
        for documentkey in doc.keys():
            value = document[documentkey]
            self.set_property(documentkey, value)

                    
    def set_property(self, property_name, value):
        for class_property in self.__dict__.keys():
            if class_property.__contains__(property_name):
                self.__dict__[class_property] = value
                break

    def to_document(self):
        """ Return the the model as a document or ```None``
            if the model properties are not setted yet
        """
        document = {}
        class_properties = self.__dict__.copy()
        for classproperty in class_properties.keys():
            documentkey = classproperty.split("__")
            documentkey = documentkey[1]
            if class_properties[classproperty] is not None:
                document[documentkey] = class_properties[classproperty]               
        
        if len(document) > 0:
            return document
        else:
            return None    

    def to_json(self):
        if len(self.to_document()) > 0:
            json = self.to_document()
            json['id'] = str(json.pop('_id'))
            json['collection'] = self.collection
            return json
        else:
            return None

def find_model(collection):
    """Return Model based on collection name"""
    for key in AbstractModel.subclasses.keys():
        if key == collection:
            return AbstractModel.subclasses[collection]()
    
    return None
