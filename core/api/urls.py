from django.urls import path, re_path

from rest_framework.authtoken.views import obtain_auth_token
from core.api.views import edocuments as edocs

apiurlpatterns = [
    path('books/<bookid>/pages/<int:pagenumber>/', edocs.BookPage.as_view(), name='book_page'),
    path('books/<bookid>', edocs.BookView.as_view(), name='book'),
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),
]