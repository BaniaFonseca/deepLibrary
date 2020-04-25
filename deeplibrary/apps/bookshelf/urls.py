from django.conf.urls import url
from bookshelf import views

urlpatterns = [
    url(r'^shelf/$', views.ShelfPageView.as_view(), name='shelf'),
    url(r'^bookdetails/$', views.BookDetailPageView.as_view(), name='bookdetail'),
]