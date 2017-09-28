from django.conf.urls import url
from . import analyze, search

urlpatterns = [
    url(r'^analyze$', analyze.logrequest, name='logrequest'),
    url(r'^(?P<keywords>[0-9a-zA-Z\_-]+)/search/$', search.search, name='search')
]