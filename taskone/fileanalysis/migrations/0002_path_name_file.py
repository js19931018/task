# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileanalysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path_name_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('endcheck', models.CharField(max_length=400)),
            ],
        ),
    ]
