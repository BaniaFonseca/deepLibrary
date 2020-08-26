from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from core.view import ViewABC
from core.storage.crud import OSCRUD

class LightWeightViewer(ViewABC):

    def __init__(self):
        super().__init__()
        self.oscrud = OSCRUD()
    
    def get(self, request, type, edocid, pages):
        #this value must come from data streamed by apache spark 
        lastpageread = 1
        return render(request, 'lwviewer/lwviewer.html',
            context={
                'type' : type, 
                'id': edocid, 
                'pages': pages,
                'page' : lastpageread
            }, 
            content_type='text/html')
    
    def get(self, request, type, pageid):
        """pageid = edocid+page  """    
        try:
            response = self.oscrud.get_object(type, pageid)
            return HttpResponse(response)
        finally:
            response.close()
            response.release_conn()