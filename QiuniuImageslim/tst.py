#coding=utf-8
import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QiuniuImageslim.settings")
django.setup()
import time
import datetime
from imageslim.models import EmployeeAttachment,EmployeeAttachmentSlimLog
KEYS=[
    'ie_0ea63c5d287840b2a9600701d8306f3e',
    'ie_43db12e4210445f1b7f18d03b7c98675',
    'ie_51ab0e48001a4b78aca1e40ee8e7ce2d',
    'ie_7393ee2589a44e5b89492cdc48d0297a',
    'ie_912594cabf3045b8b6d692dc1c4901e4',
]

for i in range(5):
    employee='employee%s'%i
    company='company%s'%i
    type=i+1
    key=KEYS[i]

    upload_by_type=0
    e=EmployeeAttachment(employee=employee,company=company,type=type,key=key,upload_by_type=upload_by_type)
    e.save()