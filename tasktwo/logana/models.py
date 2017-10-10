# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

class Logdata(models.Model):
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    s_ip = models.CharField(max_length=200)
    cs_method = models.CharField(max_length=200)
    cs_uri_stem = models.CharField(max_length=200)
    cs_uri_query = models.CharField(max_length=1000)
    s_port = models.CharField(max_length=100)
    cs_username = models.CharField(max_length=200)
    c_ip = models.CharField(max_length=100)
    cs_user_agent = models.CharField(max_length=1000)
    sc_status = models.CharField(max_length=100)
    sc_substatus = models.CharField(max_length=100)
    sc_win32_status = models.CharField(max_length=100)
    time_taken = models.CharField(max_length=100)
    lognum=models.CharField(max_length=200)
    ip_region = models.CharField(max_length=100,default=None)
    ip_city = models.CharField(max_length=100,default=None)





# Create your models here.
