# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-10 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_fireprotectiondic_infrastructuredic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=20)),
                ('reportinfo', models.CharField(max_length=120)),
                ('reportdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('reportmenu', models.CharField(max_length=50)),
            ],
        ),
    ]
