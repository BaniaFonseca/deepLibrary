from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.deepshelf.models.edocument import Book, Author, Paper
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
        book = self.crud.get_one(Book, {'year': 2015})
        demo = book
        demos = [demo for _ in range(6)]
        return render(request, 'deepshelf/deepshelf.html',
            context={'edocuments': demos}, content_type='text/html')