from django.urls import path, re_path
from apps.home.views.home import Home

urlpatterns = [
    re_path(r'^$', Home.as_view()),
]
