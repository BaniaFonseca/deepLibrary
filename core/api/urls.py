from django.urls import path, re_path

from core.api.views import edocuments as edocs

apiurlpatterns = [
    path('books/<bookid>/pages/<int:pagenumber>', edocs.BookPage.as_view(), name=' book_page'),
    path('books/<bookid>', edocs.Book.as_view(), name='book_details')
]