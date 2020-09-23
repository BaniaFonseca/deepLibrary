from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bson.objectid import ObjectId

from core.view import ViewABC
from core.api.models import edocuments as edoc
from core.storage.oscrud import OSCRUD
from core.database.crud import CRUD

oscrud = OSCRUD()
crud = CRUD()

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
    
class BookView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, bookid):
        try:
            id = ObjectId(bookid)
            book = crud.get_one(edoc.Book, {"_id": id})
            content = book.to_json()
            return Response(content)        
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND) 