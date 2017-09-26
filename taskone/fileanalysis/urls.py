from django.conf.urls import url
from . import analyze,search

urlpatterns = [
    url(r'^analyze$', analyze.traverse_list, name='traverse_list'),
    url(r'^search$', search.searchrequest, name='search')
]