from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from deepshelf.models.electronicdocument import ElectronicDocument as edoc

class DeepShelf(View):

    def get(self, request):

        ed = edoc()
        edocuments = [ed for _ in range(20)]

        return render(request, 'deepshelf/index.html',
            {'edocuments': edocuments}, 
            content_type='text/html')