import abc

from apps.core.model import ModelABC, EmbendedModelABC

class ElectronicDocument(ModelABC):

    def __init__(self):
        self.title = None
        self.year = None
        self.country = None
        self.city = None
        self.authors = None

    @property
    def authors(self):
        """list of authors, each element on the list is an instance of the class Author"""
        return self.__authors 
    
    @authors.setter
    def authors(self, authors):
        self.__authors = authors    

    @property
    def title(self):
        """The title of the edocument"""
        return self.__title 
    
    @title.setter
    def title(self, value):
        self.__title = value    

    @property
    def year(self):
        """The year that the edocument was published"""
        return int(self.__year)
    
    @year.setter
    def year(self, value):
        self.__year = value    

    @property
    def country(self):
        """The country where the edocument was published"""
        return self.__country 
    
    @country.setter
    def country(self, value):
        self.__country = value

    @property
    def city(self):
        """The city where the edocument was published"""
        return self.__city 
    
    @city.setter
    def city(self, value):
        self.__city = value


class Author(EmbendedModelABC):

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        self.__name = value    

    @property
    def description(self):
        return self.__description 
    
    @description.setter
    def description(self, value):
        self.__description = value    

    @property
    def embendeddocument(self):
        return "author"


class Book(ElectronicDocument):
    """ A class Model """

    def __init__(self):
        super().__init__()
        self.title = None
        
    @property
    def collection(self):
        return "edocument.book"

    @property
    def embendeds(self):
        return [Author]


class Paper(ElectronicDocument):
    
    def __init__(self):
        super().__init__()

    @property
    def collection(self):
        return "edocument.paper"


class Monography(ElectronicDocument):
    
    def __init__(self):
        super().__init__()

    @property
    def collection(self):
        return "edocument.monography"
