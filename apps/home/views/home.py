from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Home(View):
    
    def __init__(self):
        pass
    
    def get(self, request):
        return render(request, 'home/index.html',
            content_type='text/html')