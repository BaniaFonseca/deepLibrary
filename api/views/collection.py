from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from django.http import HttpResponse

from bson.objectid import ObjectId

from storage.oscrud import OSCRUD
from database.crud import CRUD
from models import base_model

oscrud = OSCRUD()
crud = CRUD()

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