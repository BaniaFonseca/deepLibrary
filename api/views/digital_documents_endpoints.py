from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

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
        name = resourceid+pagenumber
        pagecontent = oscrud.get_one(collection, name)
        if object is None:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        else:
            return HttpResponse(content=pagecontent, content_type='application/pdf')        
            

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
    
    def put(self, request, collection, resourceid):
        id = ObjectId(resourceid)
        model = crud.get_one(collection, {"_id": id})
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            document = JSONParser().parse(request)
            model.set_from_document(document)
            message = "The {}'s details has been properly updated".format(model.type)
            if crud.update_one(model) is not None: 
                return Response({'message': message})
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)