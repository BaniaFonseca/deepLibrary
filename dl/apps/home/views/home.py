from django.shortcuts import render

from core.view import ViewABC

class Home(ViewABC):
    
    def __init__(self):
        pass
    
    def get(self, request):
        return render(request, 'home/index.html',
            content_type='text/html')