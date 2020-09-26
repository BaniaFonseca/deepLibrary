from bson.objectid import ObjectId
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.views import View
from storage.oscrud import OSCRUD


class LightWeightViewer(View):
    pass

class PDFLoader(View):
    pass