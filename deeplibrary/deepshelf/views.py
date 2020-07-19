from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from deepshelf.models.electronic_document import ElectronicDocument as edoc

class DeepShelf(View):

    def get(self, request):

        ed = edoc()
        edocuments = [ed for _ in range(6)]

        return render(request, 'deepshelf/shelf.html',
            {'edocuments': edocuments}, 
            content_type='text/html')