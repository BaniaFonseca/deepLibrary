from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.deepshelf.models.electronicdocument import Book, Author, Paper
from apps.database.crud import CRUD

class DeepShelf(View):

    def __init__(self):   
        self.crud = CRUD()

    @property
    def crud(self):
        return self.__crud
    
    @crud.setter
    def crud(self, value):
        self.__crud = value
    
    def get(self, request):
        book = Book()

        book = self.crud.get_one(Book, {'year': 2015})
        print("booooooook {}".format(book))
        
        if book is not None:
            print("++++++++++++++= authors {}".format(book.authors))
            for i, author in enumerate(book.authors, 1):
                print("########### {} author {} {}".format(i, author.firstname, author.surname))
        
        demo = book
        demos = [demo for _ in range(6)]
        
        return render(request, 'deepshelf/deepshelf.html',
            context={'edocuments': demos}, content_type='text/html')