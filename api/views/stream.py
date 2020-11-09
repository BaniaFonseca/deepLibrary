from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from bson.objectid import ObjectId
import PyPDF2
import io

from api.models import resources
from storage.oscrud import OSCRUD
from database.crud import CRUD
from models import base_model

oscrud = OSCRUD()
crud = CRUD()

class Stream(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self, request, collection, resource_id, page_number):
        id = ObjectId(resource_id)
        criteria = {"_id": id}
        model = crud.get_one(collection, criteria)
        if model is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        page = model.index[page_number-1]
        content = self.get_page(collection, resource_id, page_number)
        print(content)
        return HttpResponse(content)

    """
        This method needs improvements because it is very inefficient
    """
    def get_page(self, collection, resource_id, page_number):
        data = oscrud.get_object(collection, resource_id)
        dataIO = io.BytesIO(data)
        pdfr = PyPDF2.PdfFileReader(dataIO)
        pdfpage = pdfr.getPage(page_number-1)
        pdw = PyPDF2.PdfFileWriter()
        pdw.addPage(pdfpage)
        with io.BytesIO() as pagedata:
            pdw.write(pagedata)
            return pagedata.getvalue()