#coding=utf-8
import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QiuniuImageslim.settings")
django.setup()
import time,threading
EmploymentAttachmentType={'1':1, '2':2, '3':3, '4':4, '5':5}
#value: 1:头像 2:证件照 3:员工证明 4:证书 5:证件图片
#key: the 'type' in table EmploymentAttachment
from qiniuslim import EmploymentAttachmentSlim
from imageslim.models import EmployeeAttachment,EmployeeAttachmentSlimLog

class Presistent_slim(object):
    # employattachment is a object to slim,got from EmployeeAttachment
    # when newupdate=True it pfop slim origin img and produces thumbnail img ,else only slim origin img
    # thumblargename/thumbsmallname to save thumbnail key such as 'originkey' + 'thumblargename'
    # thumbnail results are saving in the same bucket and path of origin img
    # use start_slim to exe a slim,the record will save in EmployeeAttachmentSlimLog
    # change EmploymentAttachmentType to get correct employee img update type
    def __init__(self,emloyeeattachment,newupdate=False,thumblargename=None,thumbsmallname=None):
        self.employeeattachment=emloyeeattachment
        self.attachment_id=emloyeeattachment.id
        self.typeid=self.convert_type(emloyeeattachment.type)
        self.key=emloyeeattachment.key
        self.newupt=newupdate
        self.tln=thumblargename
        self.tsn=thumbsmallname
        self.slimlog=EmployeeAttachmentSlimLog
        self.slim_time=time.time()
        self.done=False
        self.done_time=False
    def convert_type(self,type):
        return EmploymentAttachmentType[str(type)]

    def start_slim(self):
         e=EmploymentAttachmentSlim(self.attachment_id, self.key, self.typeid, self.newupt, self.tln, self.tsn)
         e.start_slim()
         self.get_result()
         self.save_record()

    def get_result(self):
        pass

    def save_record(self):
        s = self.slimlog(employee=self.employeeattachment,  is_slimed=self.done, down_time=self.done_time)
        s.save()
        self.employeeattachment.is_slimed=True if self.done else False

class SlimControl(object):
    # pfop with nums of img
    def __init__(self,start_num,queryset_num):
        self.slimlist = EmployeeAttachment.objects.all()[start_num:start_num+queryset_num]
        print self.slimlist
    def start_slim(self):
        for i in self.slimlist:
            p=Presistent_slim(i,newupdate=True,thumblargename=None,thumbsmallname=None)
            p.start_slim()


if __name__ == '__main__':
    s=SlimControl(0, 5)
    s.start_slim()