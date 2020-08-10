from django.urls import path, re_path

from apps.deepshelf.views.deepshelf import DeepShelf

deepshelfpatterns = [
    re_path(r'^', DeepShelf.as_view()),
]