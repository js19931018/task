# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAttachment',
            fields=[
                ('id', models.UUIDField(db_column='c_id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('employee', models.CharField(db_column='c_employee_id', max_length=100, verbose_name='\u5458\u5de5Id')),
                ('company', models.CharField(blank=True, db_column='c_company_id', max_length=500, null=True, verbose_name='\u4f01\u4e1aId')),
                ('type', models.IntegerField(db_column='c_attachment_type', default=0, verbose_name='\u9644\u4ef6\u7c7b\u578b')),
                ('key', models.CharField(blank=True, db_column='c_attachment_url', max_length=500, null=True, verbose_name='\u9644\u4ef6\u7684key')),
                ('add_by', models.CharField(db_column='c_add_by', max_length=100, null=True, verbose_name='\u6dfb\u52a0\u4eba')),
                ('add_dt', models.DateTimeField(auto_now_add=True, db_column='c_add_dt', verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('update_by', models.CharField(blank=True, db_column='c_update_by', max_length=300, null=True, verbose_name='\u4fee\u6539\u4eba')),
                ('update_dt', models.DateTimeField(auto_now=True, db_column='c_update_dt', null=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('sort', models.IntegerField(blank=True, db_column='c_sort', default=0, verbose_name='\u6392\u5e8f')),
                ('filename', models.CharField(blank=True, db_column='c_filename', max_length=50, null=True, verbose_name='\u9644\u4ef6\u6587\u4ef6\u540d')),
                ('filename_ext', models.CharField(blank=True, db_column='c_filename_ext', max_length=10, null=True, verbose_name='\u6587\u4ef6\u6269\u5c55\u540d')),
                ('file_size', models.IntegerField(blank=True, db_column='c_file_size', null=True, verbose_name='\u6587\u4ef6\u5927\u5c0f')),
                ('is_delete', models.BooleanField(db_column='c_is_delete', default=False)),
                ('is_slimed', models.BooleanField(db_column='c_is_slimed', default=False)),
                ('view_name', models.CharField(blank=True, db_column='c_view_name', max_length=200, null=True, verbose_name='\u6587\u4ef6\u663e\u793a\u540d\u79f0')),
                ('upload_by', models.UUIDField(db_column='c_upload_by', default=uuid.uuid4, verbose_name='\u4e0a\u4f20\u4eba\u7684id')),
                ('upload_by_name', models.CharField(db_column='c_upload_by_name', default='', max_length=30, verbose_name='\u4e0a\u4f20\u4eba\u59d3\u540d')),
                ('upload_by_type', models.IntegerField(db_column='c_upload_by_type', verbose_name='\u4e0a\u4f20\u4eba\u7c7b\u578b')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAttachmentSlimLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slim_time', models.DateTimeField(db_column='c_slim_time')),
                ('down_time', models.DateTimeField(db_column='c_down_time', null=True)),
                ('key', models.CharField(blank=True, db_column='c_attachment_url', max_length=500, null=True, verbose_name='\u9644\u4ef6\u7684key')),
                ('persistent_id', models.CharField(db_column='c_persistent_id', max_length=100, null=True, verbose_name='\u6570\u636e\u5904\u7406ID')),
                ('is_slimed', models.BooleanField(db_column='c_is_slimed', default=False)),
                ('employee', models.ForeignKey(db_column='employeeattachment_id', on_delete=django.db.models.deletion.CASCADE, to='imageslim.EmployeeAttachment')),
            ],
        ),
    ]
