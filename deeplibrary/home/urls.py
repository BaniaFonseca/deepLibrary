from django.conf.urls import url
from home.views import *

urlpatterns = [
    url('', Home.as_view(), name='home'),
]
