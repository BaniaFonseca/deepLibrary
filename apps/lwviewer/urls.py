from django.urls import path, re_path

from apps.lwviewer.views.lwviewer import (
                                            LightWeightViewer,
                                            LightWeightPDFLoader)

lwviewerpatterns = [
    path('', LightWeightViewer.as_view()),
    path('pdfloader', LightWeightPDFLoader.as_view())
]
