from django.urls import path, re_path, include

from apps.lwviewer.views.lwviewer import(
    LightWeightViewer,
    PDFLoader)

lwviewerpatterns = [
    path('<collection>/<id>/', LightWeightViewer.as_view(), name='viewer'),
    path('<collection>/<id>/<int:page>/', PDFLoader.as_view(), name='pdfloader')
]
