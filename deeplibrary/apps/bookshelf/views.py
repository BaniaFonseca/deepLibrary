# djangotemplates/example/views.py
from django.shortcuts import render
from django.views.generic import TemplateView 

class ShelfPageView(TemplateView):
    template_name = "shelf.html"


class BookDetailPageView(TemplateView):
    template_name = "bookdetail.html"