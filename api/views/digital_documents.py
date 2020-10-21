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
from models import base_model

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
            

class Collection(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, collection):
        if base_model.find_model(collection) is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        models = crud.get_many(collection)
        content = []
        for model in models:
            content.append(model.to_json())
        return Response(content)

    def post(self, request, collection):
        model = base_model.find_model(collection)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        doc = JSONParser().parse(request)
        model.set_from_document(doc)
        if crud.insert_one(model) is None:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            message = "The resource has been succefully added"
            return Response({'message': message})
        
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
            message = "The resource's details has been properly updated"
            if crud.update_one(model) is not None: 
                return Response({'message': message})
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)