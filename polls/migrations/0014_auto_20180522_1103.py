# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-22 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20180516_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reportdate',
            field=models.CharField(default='Tue May 22 11:03:16 2018', max_length=120),
        ),
    ]
