from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from bson.objectid import ObjectId

from core.view import ViewABC
from core.api.models import edocuments as edoc
from core.storage.oscrud import OSCRUD

oscrud = OSCRUD()

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super().__init__(content=content, **kwargs)

class PDFResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs['content_type'] = 'application/pdf'
        super().__init__(content=data, **kwargs)


class BookPage(ViewABC):
    @csrf_exempt
    def get(self, request, bookid, pagenumber):
        try:
            objectname = bookid+str(pagenumber)
            page = oscrud.get_object('books', objectname)
            return PDFResponse(data=page)        
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

class Book(ViewABC):
    @csrf_exempt
    def get(self, request, bookid):
        try:
            id = ObjectId(bookid)
            book = self.crud.get_one(edoc.Book, {"_id": id})
            return JSONResponse(book.to_json())        
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
