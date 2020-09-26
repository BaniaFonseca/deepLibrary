from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bson.objectid import ObjectId

from api.models import digital_documents as ddoc
from storage.oscrud import OSCRUD
from database.crud import CRUD

oscrud = OSCRUD()
crud = CRUD()



class BookPage(APIView):
    pass

class BookView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, bookid):
        try:
            id = ObjectId(bookid)
            book = crud.get_one(edoc.Book, {"_id": id})
            content = book.to_json()
            return Response(content)        
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND) 