from bson.objectid import ObjectId
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponse, Http404

from core.view import ViewABC
from core.storage.oscrud import OSCRUD
from apps.deepshelf.models.edocument import Book

#just for development
from core.storage.demo.demo import get_page

class LightWeightViewer(ViewABC):

    def __init__(self):
        super().__init__()
        
    def get(self, request, collection, id):
        doc = self.crud.get_document(collection, {"_id": ObjectId(id)})
        return render(request, 
        'lwviewer/lwviewer.html', 
        context={'id': id, 'collection': collection, 'pages' : doc['pages'], "page":1},
        content_type="text/html")

class PDFLoader(ViewABC):

    def __init__(self):
        super().__init__()
        self.oscrud = OSCRUD()
    
    def get(self, request, collection, id,  page):    
        try:
            response = self.oscrud.get_object(collection, id+str(page))
            return HttpResponse(content=response, content_type="appplication/pdf")
        except:
            ## just for development
            content = get_page(id+str(page))
            return HttpResponse(content=content, content_type="appplication/pdf")