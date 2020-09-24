from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from bson.objectid import ObjectId

from core.database.crud import CRUD

crud = CRUD()

class PageStream(APIView):
    
    def __init__(self):
        self.collection = None

    @property
    def collection(self):
        return self.__collection
        
    @collection.setter
    def collection(self, value):
        self.__collection = value

class Resource(APIView):

    permission_classes = (IsAuthenticated,)
    
    def __init__(self):
        self.collection = None

    @property
    def collection(self):
        return self.__collection
        
    @collection.setter
    def collection(self, value):
        self.__collection = value

    def get(self, request, id):
        try:
            id = ObjectId(id)
            book = crud.get_one(edoc.Book, {"_id": id})
            content = book.to_json()
            return Response(content)        
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND) 