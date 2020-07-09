from django.urls import path
from deepshelf.views import *

urlpatterns = [
    path('about/', DeepShelf.as_view()),
]