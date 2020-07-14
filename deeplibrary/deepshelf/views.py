from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

class DeepShelf(View):

    def get(self, request):
        # < logic here >
        app_name = 'DeepShelf'
        return render(request, 'deepshelf/index.html',
        {'app_name': app_name}, content_type='text/html')