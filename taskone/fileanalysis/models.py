# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

class Path_and_name(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)

class Path_name_file(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    endcheck = models.CharField(max_length=400)
# Create your models here.
