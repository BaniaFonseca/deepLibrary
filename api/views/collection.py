from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from django.http import HttpResponse

from bson.objectid import ObjectId

from database.crud import CRUD
from models import base_model

crud = CRUD()

class Collection(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request, collection):
        if base_model.find_model(collection) is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        models = crud.get_many(collection)
        data = []
        for model in models:
            data.append(model.to_json())
        return Response(data)

    def post(self, request, collection):
        model = base_model.find_model(collection)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        model.set_from_document(request.data)
        crud.insert_one(model)    
        message = "The resource has been succefully added"
        return Response({'message': message})