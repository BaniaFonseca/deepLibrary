from django.urls import path, re_path

from apps.lwviewer.views.lwviewer import LightWeightViewer

lwviewerpatterns = [
    re_path(r'^', LightWeightViewer.as_view())
]
