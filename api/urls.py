from django.urls import path, re_path

from rest_framework.authtoken.views import obtain_auth_token
from api.views import digital_documents as dd

urlpatterns = [
    path('<collection>/<resourceid>/pages/<pagenumber>/', dd.PageView.as_view(), name='page'),
    path('<collection>/<resourceid>/', dd.DigitalDocumentView.as_view(), name='digital-document'),
    path('<collection>/', dd.Collection.as_view(), name='digital-document-collection'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]