# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogtitle', models.CharField(max_length=120)),
                ('blogcontent', models.TextField()),
            ],
        ),
    ]
