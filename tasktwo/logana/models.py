# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

class Logdata(models.Model):
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    s_ip = models.CharField(max_length=50)
    cs_method = models.CharField(max_length=5)
    cs_uri_stem = models.CharField(max_length=50)
    cs_uri_query = models.CharField(max_length=50)
    s_port = models.CharField(max_length=5)
    cs_username = models.CharField(max_length=50)
    c_ip = models.CharField(max_length=15)
    cs_user_agent = models.CharField(max_length=50)
    sc_status = models.CharField(max_length=3)
    sc_substatus = models.CharField(max_length=1)
    sc_win32_status = models.CharField(max_length=1)
    time_taken = models.CharField(max_length=6)
    lognum=models.CharField(max_length=10)



# Create your models here.
