import abc

from apps.model.model import ModelABC, EmbendedModelABC

class ElectronicDocument(ModelABC):


    @property
    def title(self):
        return self.__title 
    
    @title.setter
    def title(self, valeu):
        self.__title = valeu    

    

class Author(EmbendedModelABC):


    def __init__(self, firstname=None, surname=None):
        self.firstname = firstname
        self.surname = surname

    @property
    def firstname(self):
        return self.__firstname 
    
    @firstname.setter
    def firstname(self, valeu):
        self.__firstname = valeu    

    @property
    def surname(self):
        return self.__surname 
    
    @surname.setter
    def surname(self, valeu):
        self.__surname = valeu    

    @property
    def embendeddocument(self):
        return "author"


class Book(ElectronicDocument):
    """ A class Model """

    def __init__(self):
        super().__init__()
        self.title = None
        self.authors = None

    @property
    def authors(self):
        """list of authors, each element of the list is an instance of the class Author"""
        return self.__authors 
    
    @authors.setter
    def authors(self, authors):
        self.__authors = authors    

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



# book = Book()

# authors = [Author(firstname="Bania", surname="Fonseca"), Author(firstname="Felermino", surname="Ali")]
# for author in authors:
#     print(author.__dict__)

# book.set_from_document({'title': "Bom dia", 'authors': authors})

# print(book.title)

# doc = book.get_as_document()

# print("doc {}".format(doc))

# print()