from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from core.view import ViewABC
from core.api.streamdocs import models
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

@csrf_exempt
def stream_book_page(request, id, pagenumber):
    if request.method  == 'GET':
        try:
            page = oscrud.get_object('books', id+pagenumber)
            return PDFResponse(data=page)        
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)