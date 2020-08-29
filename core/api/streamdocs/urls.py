from django.urls import path, re_path

from core.api.streamdocs import views
streamdocsurlpatterns = [
    path('books/<id>/pages/<pagenumber>', views.stream_book_page, name='stream_book_page')
]