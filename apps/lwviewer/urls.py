from django.urls import path, re_path

from apps.lwviewer.views.lwviewer import  LightWeightViewer

lwviewerpatterns = [
    path('<type>/<edocid>/<pages>/', LightWeightViewer.as_view()),
    path('<type>/<pageid>/', LightWeightViewer.as_view())
]
