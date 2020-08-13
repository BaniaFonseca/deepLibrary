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


class Book(ElectronicDocument):
    """ A Book class Model """

    def __init__(self):
        super().__init__()
        self.publisher = None
        self.pages = None
        self.preface = None
        self.isbn = None
        self.volume = None
        self.edition = None
        self.language = None

    @property
    def language(self):
        """The book language"""
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value
    
    @property
    def edition(self):
        """The book edition"""
        return self.__edition

    @edition.setter
    def edition(self, value):
        self.__edition = value

    @property
    def publisher(self):
        """The book publisher"""
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        self.__publisher = value

    @property
    def pages(self):
        """The number of pages the book have"""
        return self.__pages

    @pages.setter
    def pages(self, value):
        self.__pages = value

    @property
    def preface(self):
        """The book's preface"""
        return self.__preface

    @preface.setter
    def preface(self, value):
        self.__preface = value

    @property
    def isbn(self):
        """The book's ISBN"""
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value

    @property
    def volume(self):
        """The book's volume"""
        return self.__volume

    @isbn.setter
    def volume(self, value):
        self.__volume = value
    
    @property
    def collection(self):
        return "edocument.book"

    @property
    def embendeds(self):
        return [Author]


class Paper(ElectronicDocument):
    """ A Paper class model"""
    def __init__(self):
        super().__init__()
        self.keywords = None
        self.pages = None
        self.abstract = None
        self.volume = None
        self.doi = None
        self.urls = None
        self.publisher = None
        self.arxivid = None 

    
    @property
    def arxivid(self):
        """The paper's arXiv ID"""
        return self.__arxivid

    @arxivid.setter
    def arxividr(self, value):
        self.__arxivid = value

    @property
    def publisher(self):
        """The paper's publisher"""
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        self.__publisher = value

    @property
    def urls(self):
        """The paper's urls """
        return self.__urls

    @urls.setter
    def urls(self, value):
        self.__urls = value

    
    @property
    def doi(self):
        """The paper's DOI """
        return self.__doi

    @doi.setter
    def doi(self, value):
        self.__doi = value

    @property
    def abstract(self):
        """ The paper's abstract"""
        return self.__abstract

    @abstract.setter
    def abstract(self, value):
        self.__abstract = value

    @property
    def keywords(self):
        """ The paper keywords, is a list os strings """
        return self.__keywords

    @keywords.setter
    def keywords(self, value):
        self.__keywords = value

    @property
    def volume(self):
        """The book's volume"""
        return self.__volume


    @property
    def pages(self):
        """The number of pages the paper have"""
        return self.__pages

    @pages.setter
    def pages(self, value):
        self.__pages = value


    @property
    def collection(self):
        return "edocument.paper"


class Monography(ElectronicDocument):
    """A  Monography class model"""
    def __init__(self):
        super().__init__()
        self.keywords = None
        self.pages = None
        self.abstract = None
        self.university = None
        self.objective = None

    @property
    def university(self):
        """The of the university"""
        return self.__university

    @university.setter
    def university(self, value):
        self.__university = value

    @property
    def pages(self):
        """The number of pages the monography have"""
        return self.__pages

    @pages.setter
    def pages(self, value):
        self.__pages = value

    @property
    def abstract(self):
        """ The monography's abstract"""
        return self.__abstract

    @abstract.setter
    def abstract(self, value):
        self.__abstract = value

    @property
    def keywords(self):
        """ The monography keywords, is a list os strings """
        return self.__keywords

    @keywords.setter
    def keywords(self, value):
        self.__keywords = value

    @property
    def collection(self):
        return "edocument.monography"


class Author(EmbendedModelABC):
    """ An  Author Embended Mode"""
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
