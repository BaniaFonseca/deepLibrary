from django.urls import path, re_path
from deepshelf.views import *

urlpatterns = [
    re_path(r'^', DeepShelf.as_view()),
]