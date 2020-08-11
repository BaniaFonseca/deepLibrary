import abc
from django.http import HttpResponse
from django.views import View

from apps.core.database.crud import CRUD

class ViewABC(View):

    def __init__(self):   
        self.crud = CRUD()

    @property
    def crud(self):
        return self.__crud
    
    @crud.setter
    def crud(self, value):
        self.__crud = value
