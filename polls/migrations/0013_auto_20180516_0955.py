# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-16 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='coolingstationdic',
            name='readonly_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='coolingstationdic',
            name='rw_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='coolingstationdic',
            name='unvisible_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='elictricdic',
            name='readonly_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='elictricdic',
            name='rw_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='elictricdic',
            name='unvisible_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='fireprotectiondic',
            name='readonly_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='fireprotectiondic',
            name='rw_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='fireprotectiondic',
            name='unvisible_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='infrastructuredic',
            name='readonly_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='infrastructuredic',
            name='rw_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
        migrations.AddField(
            model_name='infrastructuredic',
            name='unvisible_users',
            field=models.CharField(default='[]', max_length=1200),
        ),
    ]