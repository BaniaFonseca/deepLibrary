from django.urls import path, re_path

from rest_framework.authtoken.views import obtain_auth_token
from api.views import collection, resource, content, stream


urlpatterns = [
    path('<collection>/<resource_id>/', resource.Resource.as_view(), name='dl-resource'),
    path('<collection>/', collection.Collection.as_view(), name='dl-collection'),
    path('<collection>/<resource_id>/content/', content.Content.as_view(), name="dl-content"),
    path("<collection>/<resource_id>/page/<int:page_number>/", stream.Stream.as_view(), name='dl-stream'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]