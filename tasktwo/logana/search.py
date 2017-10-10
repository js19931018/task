'''search(path,*args) return a list contain result
if path is sql,search in sql,else search in a json file with the path,
args are keywords  see save-to-data to store data in sql'''





import os
import django
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskone.settings")
django.setup()


from logana.models import Logdata
from django.http import HttpResponse
import json
import logging

from django.shortcuts import render

def search(request, keywords):

    return HttpResponse('get keywords')













