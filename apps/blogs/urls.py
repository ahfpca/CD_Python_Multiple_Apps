from django.conf.urls import url
from . import views


urlpatterns = [
    url('new$', views.new),
    url('create$', views.create),
    url(r'(?P<id>\d+)/edit', views.edit),
    url(r'(?P<id>\d+)/delete', views.destroy),
    url(r'(?P<id>\d+)$', views.show),
    url(r'^', views.index),
]
