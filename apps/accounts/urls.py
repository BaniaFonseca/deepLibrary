from django.conf.urls import url
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from apps.accounts import views

from dl.settings import common
urlpatterns = [
    url(r'signup/$', views.SignUpView.as_view(), name='signup'),
]