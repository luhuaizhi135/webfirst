# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-07 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_blog_blogabstract'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElictricDic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electric_item', models.CharField(max_length=120)),
            ],
        ),
    ]
