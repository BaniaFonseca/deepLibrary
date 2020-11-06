from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, BaseParser


from django.http import HttpResponse

from bson.objectid import ObjectId

import io

from api.models import resources
from storage.oscrud import OSCRUD
from database.crud import CRUD
from models import base_model

import PyPDF2
import io

oscrud = OSCRUD()
crud = CRUD()

class PDFParser(BaseParser):
    """
    docstring
    """
    media_type = 'application/pdf'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()


class Content(APIView):
    
    permission_classes = (IsAuthenticated,)
    parser_classes = [PDFParser, JSONParser]

    def post(self, request, collection, resourceid):
        id = ObjectId(resourceid)
        criteria = {"_id": id}
        model = crud.get_one(collection, criteria)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            with io.BytesIO(request.data) as data:
                oscrud.put_object(collection, resourceid, data, 
                    len(data.getvalue()), "application/pdf")    
        return Response({"message": "Content inserted successfully!"})

    def put(self, request, collection, resourceid):
        id = ObjectId(resourceid)
        criteria = {"_id": id}
        model = crud.get_one(collection, criteria)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            with io.BytesIO(request.data) as data:
                oscrud.put_object(collection, resourceid,
                    data, len(data.getvalue()), "application/pdf")
        return Response({"message": "Content Updated successfully!"})

    def delete(self, request, collection, resourceid):
        id = ObjectId(resourceid)
        criteria = {"_id": id}
        model = crud.get_one(collection, criteria)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            
            return Response({"message": "Content deleted sucessfully"})