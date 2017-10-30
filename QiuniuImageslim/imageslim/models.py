# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

class EmployeeAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_column='c_id')
    employee = models.CharField(verbose_name='员工Id', max_length=100, db_column="c_employee_id")
    company = models.CharField(verbose_name='企业Id', max_length=500, null=True, blank=True, db_column='c_company_id')
    type = models.IntegerField(verbose_name='附件类型', default=0, db_column="c_attachment_type")


    key = models.CharField(verbose_name='附件的key', max_length=500, null=True, blank=True, db_column='c_attachment_url')
    add_by = models.CharField( verbose_name="添加人", null=True, db_column="c_add_by", max_length=100)
    add_dt = models.DateTimeField(verbose_name="添加时间", auto_now_add=True, db_column="c_add_dt")
    update_by = models.CharField(verbose_name='修改人', blank=True, null=True, db_column='c_update_by', max_length=300)
    update_dt = models.DateTimeField(verbose_name='修改时间', blank=True, null=True, db_column='c_update_dt', auto_now=True)
    sort = models.IntegerField('排序', db_column='c_sort', blank=True, default=0)
    filename = models.CharField('附件文件名', max_length=50, db_column='c_filename', blank=True, null=True)
    filename_ext = models.CharField('文件扩展名', max_length=10, db_column='c_filename_ext', blank=True, null=True)
    file_size = models.IntegerField('文件大小', db_column='c_file_size', blank=True, null=True)
    is_delete = models.BooleanField(default=False, db_column='c_is_delete')
    is_slimed = models.BooleanField(default=False, db_column='c_is_slimed')
    view_name = models.CharField('文件显示名称', max_length=200, db_column='c_view_name', blank=True, null=True)

    upload_by = models.UUIDField("上传人的id", default=uuid.uuid4, db_column="c_upload_by")
    upload_by_name = models.CharField("上传人姓名", max_length=30, default="", db_column="c_upload_by_name")
    upload_by_type = models.IntegerField("上传人类型",  db_column="c_upload_by_type")

# Create your models here.
class EmployeeAttachmentSlimLog(models.Model):
    employee=models.ForeignKey(EmployeeAttachment, db_column='employeeattachment_id')
    slim_time=models.DateTimeField(db_column='c_slim_time',auto_now=True)
    down_time=models.DateTimeField(null=True,db_column='c_down_time',auto_now=True)
    key = models.CharField(verbose_name='附件的key', max_length=500, null=True, blank=True, db_column='c_attachment_url')
    persistent_id= models.CharField(verbose_name='数据处理ID',max_length=100,null=True,db_column='c_persistent_id')
    is_slimed=models.BooleanField(default=False,db_column='c_is_slimed')




