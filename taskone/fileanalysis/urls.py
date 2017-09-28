from django.conf.urls import url
from . import analyze, search

urlpatterns = [
    url(r'^analyze$', analyze.analyzerequest, name='analyzerequest'),
    url(r'^(?P<pathkey>[0-9a-zA-Z\_-]+)/search/$', search.searchrequest, name='search')
]