# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-03-12 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etvf', '0018_auto_20200312_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kristiana',
            name='user',
        ),
    ]
