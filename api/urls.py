from django.urls import path, re_path

from rest_framework.authtoken.views import obtain_auth_token
from api.views import digital_documents_endpoints as dde

urlpatterns = [
    path('<collection>/<resourceid>/pages/<int:pagenumber>', dde.PageView.as_view(), name='page-stream'),
    path('<collection>/<resourceid>', dde.DigitalDocumentView.as_view(), name='digital-document'),
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),
]