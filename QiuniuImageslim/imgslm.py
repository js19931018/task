#coding=utf-8
import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QiuniuImageslim.settings")
django.setup()
import time,threading
EmploymentAttachmentType={'1':1, '2':2, '3':3, '4':4, '5':5}
#value: 1:头像 2:证件照 3:员工证明 4:证书 5:证件图片
#key: the 'type' column in table EmploymentAttachment
from qiniuslim import EmploymentAttachmentSlim
from imageslim.models import EmployeeAttachment,EmployeeAttachmentSlimLog
import json

class Presistent_slim(object):
    # employattachment is a object to slim,got from table EmployeeAttachment,it must has "key","id","type" columns
    # or you can use at_id ,key,typeid instead using data from table EmployeeAttachment
    # if newupdate=True, it pfop slim origin img and produces thumbnail img ,else only slim origin img
    # thumblargename/thumbsmallname to save thumbnail key such as 'originkey' + 'thumblargename'
    # thumbnail results are saving in the same bucket and path of origin img
    # use start_slim to execute a slim,the record will save in EmployeeAttachmentSlimLog
    # change EmploymentAttachmentType to get correct employee img update type
    def __init__(self,emloyeeattachment=None,newupdate=False,thumblargename=None,thumbsmallname=None,at_id=None,typeid=None,key=None):
        self.employeeattachment=emloyeeattachment
        self.attachment_id=emloyeeattachment.id if emloyeeattachment else at_id
        self.typeid=self.convert_type(emloyeeattachment.type) if emloyeeattachment else typeid
        self.key=emloyeeattachment.key if emloyeeattachment else key
        self.newupt=newupdate
        self.tln=thumblargename
        self.tsn=thumbsmallname
        self.slimlog=EmployeeAttachmentSlimLog
        self.slim_time=time.time()
        self.done=False
        self.done_time=False
        self.imginfo=None
        self.imgsize=None

    def convert_type(self,type):
        return EmploymentAttachmentType[str(type)]

    def start_slim(self):
        e=EmploymentAttachmentSlim(self.attachment_id, self.key, self.typeid, self.newupt, self.tln, self.tsn)
        e.start_slim()
        self.get_result()
        self.imginfo=e.get_img_info()

        self.imgsize=json.loads(self.imginfo)['size']



        self.save_record() # or use your own method to save result

    def get_result(self):
        pass

    def save_record(self):   #use for tests
        s = self.slimlog(employee=self.employeeattachment,  is_slimed=self.done, down_time=self.done_time,got_size=False if self.imgsize==None else True)
        s.save()
        self.employeeattachment.is_slimed=True if self.done else False
        if self.imgsize:
           self.employeeattachment.file_size=self.imgsize
           self.employeeattachment.save()
        elif self.done:
           self.employeeattachment.file_size='unknown'
           self.employeeattachment.save()
        else:
           pass

    def save_record_own(self):
        pass

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