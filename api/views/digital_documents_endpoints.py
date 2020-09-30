from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from bson.objectid import ObjectId

from api.models import digital_documents as ddoc
from storage.oscrud import OSCRUD
from database.crud import CRUD

oscrud = OSCRUD()
crud = CRUD()


class PageView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, collection, resourceid, pagenumber):
        name = resourceid+str(pagenumber)
        object = oscrud.get_one(collection, name)
        if object is None:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        else:
            return HttpResponse(content=object, content_type='application/pdf')        
            

class DigitalDocumentView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, collection, resourceid):
            id = ObjectId(resourceid)
            model = crud.get_one(collection, {"_id": id})
            if model is None:
                return Response(status=status.HTTP_404_NOT_FOUND) 
            else:
                content = model.to_json()
                return Response(content)        
            