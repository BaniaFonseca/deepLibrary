from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from django.http import HttpResponse

from bson.objectid import ObjectId

from api.models import resources
from storage.oscrud import OSCRUD
from database.crud import CRUD
from models import base_model

oscrud = OSCRUD()
crud = CRUD()
        
class Resource(APIView):
    
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
            message = "The resource's details has been properly updated"
            if crud.update_one(collection, document, {'_id': id}) is not None: 
                return Response({'message': message})
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, collection, resourceid):
        id = ObjectId(resourceid)
        criteria = {"_id": id}
        model = crud.get_one(collection, criteria)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            message = "The resouce had been successfully deleted"
            crud.delete_one(collection, criteria)
            return Response({"message": message})