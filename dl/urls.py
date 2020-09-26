from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('apps.home.urls')),
    re_path('deepshelf/', include('apps.deepshelf.urls')),
    re_path('read/', include('apps.lwviewer.urls')),
    path('api/', include('api.urls')), 
    path('accounts/',  include('django.contrib.auth.urls')),
]