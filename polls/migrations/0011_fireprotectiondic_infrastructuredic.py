# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-09 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20180509_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='FireProtectionDic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='infrastructureDic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=120)),
            ],
        ),
    ]
