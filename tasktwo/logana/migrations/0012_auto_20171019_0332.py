# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logana', '0011_auto_20171019_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipnet',
            name='id',
        ),
        migrations.AlterField(
            model_name='ipnet',
            name='ip',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
