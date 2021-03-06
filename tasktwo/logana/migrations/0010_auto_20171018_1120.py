# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logana', '0009_clientip_regionid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ipnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Netregion',
            fields=[
                ('net', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=100)),
                ('iptype', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Regioncount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('num', models.IntegerField(max_length=20)),
                ('logdatename', models.DateField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Clientip',
        ),
        migrations.AddField(
            model_name='ipnet',
            name='net',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logana.Netregion'),
        ),
    ]
