from django.contrib import admin
from django.urls import include, path, re_path

from apps.home.urls import homepatterns
from apps.deepshelf.urls import deepshelfpatterns 
from apps.lwviewer.urls import lwviewerpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(homepatterns)),
    re_path('deepshelf/', include(deepshelfpatterns)),
    re_path('lwviewer/', include(lwviewerpatterns))
]