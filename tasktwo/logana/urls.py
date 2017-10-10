from django.conf.urls import url
from . import analyze, search

urlpatterns = [
    url(r'^analyze$', analyze.logrequest, name='logrequest'),
    url(r'^(?P<keywords>[0-9a-zA-Z\_-]+)/search/$', search.search, name='search'),
    url(r'^check_region$', analyze.check_id, name='check_id'),
    url(r'^analyze_quick', analyze.logrequest_skethy, name='logrequest_skethy'),
    url(r'^get_quick_check_id', analyze.get_quick_check_id, name='quick_check_id'),
]