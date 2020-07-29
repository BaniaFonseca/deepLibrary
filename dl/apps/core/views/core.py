from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class DeepLibraryBaseView(View):

    def __init__(self):
        self.context = []
        super().__init__()
