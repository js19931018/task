# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logana', '0008_auto_20171012_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Regionid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.IntegerField(max_length=50)),
                ('c_name', models.CharField(max_length=50)),
                ('c_pid', models.IntegerField(max_length=50)),
                ('c_sina_code', models.CharField(max_length=50)),
                ('c_sina_id', models.IntegerField(max_length=50)),
                ('C_sina_pid', models.IntegerField(max_length=50)),
                ('c_alias', models.CharField(max_length=50)),
                ('c_pinyin', models.CharField(max_length=50)),
                ('c_pinyin_lite', models.CharField(max_length=50)),
                ('c_sort', models.CharField(max_length=50)),
            ],
        ),
    ]
