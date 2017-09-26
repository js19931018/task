# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

class Path_and_name(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)

# Create your models here.
