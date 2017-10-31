# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageslim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeattachmentslimlog',
            name='got_size',
            field=models.BooleanField(db_column='c_got_size', default=False),
        ),
        migrations.AlterField(
            model_name='employeeattachmentslimlog',
            name='down_time',
            field=models.DateTimeField(auto_now=True, db_column='c_down_time', null=True),
        ),
        migrations.AlterField(
            model_name='employeeattachmentslimlog',
            name='slim_time',
            field=models.DateTimeField(auto_now=True, db_column='c_slim_time'),
        ),
    ]
