from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url

from apps.home.urls import homepatterns
from apps.deepshelf.urls import deepshelfpatterns 
from apps.lwviewer.urls import lwviewerpatterns
from core.api.urls import apiurlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(homepatterns)),
    re_path('deepshelf/', include(deepshelfpatterns)),
    re_path('read/', include(lwviewerpatterns)),
    path('api/', include(apiurlpatterns)), 
    path('accounts/',  include('django.contrib.auth.urls')),
]