# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]