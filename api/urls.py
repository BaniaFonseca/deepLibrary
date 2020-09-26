from django.urls import path, re_path

from rest_framework.authtoken.views import obtain_auth_token
from api.views import digital_documents_endpoints as dde

urlpatterns = [
    path('books/<bookid>/pages/<int:pagenumber>/', dde.BookPage.as_view(), name='book_page'),
    path('books/<bookid>', dde.BookView.as_view(), name='book'),
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),
]