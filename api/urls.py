from django.urls import path, re_path

from rest_framework.authtoken.views import obtain_auth_token
from api.views import collection, resource

urlpatterns = [
    path('<collection>/<resourceid>/', resource.Resource.as_view(), name='dl-resource'),
    path('<collection>/', collection.Collection.as_view(), name='dl-collection'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]