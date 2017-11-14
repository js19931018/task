# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

class Logdata(models.Model):
    date = models.DateField(max_length=200)
    time = models.TimeField(max_length=200)
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

class Netregion(models.Model):
    net=models.CharField(max_length=100, primary_key=True)
    region=models.CharField(max_length=100)
    iptype=models.CharField(max_length=100)
    version=models.CharField(max_length=100)


class Ipnet(models.Model):
    ip=models.CharField(max_length=100, primary_key=True)
    net=models.CharField(max_length=100)



class Regioncount(models.Model):
    region = models.CharField(max_length=100)
    num = models.IntegerField(max_length=20)
    logdatename = models.CharField(max_length=100)



class Regionid(models.Model):
    c_id = models.IntegerField(max_length=50)
    c_name = models.CharField(max_length=50)
    c_pid =models.IntegerField(max_length=50)
    c_sina_code = models.CharField(max_length=50)
    c_sina_id = models.IntegerField(max_length=50)
    C_sina_pid = models.IntegerField(max_length=50)
    c_alias= models.CharField(max_length=50)
    c_pinyin =models.CharField(max_length=50)
    c_pinyin_lite =models.CharField(max_length=50)
    c_sort=models.CharField(max_length=50)


class Analyzedata(models.Model):
    time =models.CharField(max_length=50)
    ip_message=models.TextField(max_length=30000)
    page_massage=models.TextField(max_length=30000)









# Create your models here.
