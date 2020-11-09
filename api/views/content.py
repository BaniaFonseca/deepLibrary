from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, BaseParser
from rest_framework.renderers import BaseRenderer
from django.http import HttpResponse
from bson.objectid import ObjectId
import io
import PyPDF2

from api.models import resources
from storage.oscrud import OSCRUD
from database.crud import CRUD
from models import base_model

oscrud = OSCRUD()
crud = CRUD()

class PDFParser(BaseParser):
    """
    docstring
    """
    media_type = 'application/pdf'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()


class PDFRenderer(BaseRenderer):
    media_type = 'application/pdf'
    format = 'pdf'

    def render(self, data, media_type=None, renderer_context=None):
        return data

class Content(APIView):
    
    permission_classes = (IsAuthenticated,)
    parser_classes = [PDFParser, JSONParser]
    rederer_classes = [PDFRenderer]

    def post(self, request, collection, resource_id):
        id = ObjectId(resource_id)
        criteria = {"_id": id}
        model = crud.get_one(collection, criteria)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            with io.BytesIO(request.data) as data:
                data.seek(0)
                oscrud.put_object(collection, resource_id,
                    data, len(data.getvalue()), "application/pdf")    
        return Response({"message": "Content inserted successfully!"})

    def put(self, request, collection, resource_id):
        id = ObjectId(resource_id)
        criteria = {"_id": id}
        model = crud.get_one(collection, criteria)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            with io.BytesIO(request.data) as data:
                data.seek(0)
                oscrud.put_object(collection, resource_id,
                    data, len(data.getvalue()), "application/pdf")
        return Response({"message": "Content Updated successfully!"})

    def delete(self, request, collection, resource_id):
        id = ObjectId(resource_id)
        criteria = {"_id": id}
        model = crud.get_one(collection, criteria)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Content deleted sucessfully"})
    
    # def create_index(self, collection, resource_id, data):
    #     criteria = {"_id": ObjectId(resource_id)}
    #     index = []
    #     total_nbytes = 0
    #     pdfr = PyPDF2.PdfFileReader(data) 
    #     npages = pdfr.numPages
    #     for i in range(npages):
    #         page = pdfr.getPage(i)
    #         pdw = PyPDF2.PdfFileWriter()
    #         pdw.addPage(page) 
    #         with io.BytesIO() as pagedata:
    #             pdw.write(pagedata)
    #             # nbytes = pagedata.tell()
    #             nbytes = len(pagedata.getvalue())
    #             pagedata.seek(0)
    #             index.append({"page": i+1, "offset": total_nbytes, "length": nbytes})
    #             total_nbytes = total_nbytes + nbytes
    #     crud.update_one(collection, {"index": index}, criteria)