from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('home.urls')),
    re_path('deepshelf/', include('deepshelf.urls'))
]