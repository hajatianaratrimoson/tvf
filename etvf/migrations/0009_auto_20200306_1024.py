# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-03-06 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etvf', '0008_auto_20200305_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitapo',
            name='vola_vina',
        ),
        migrations.AddField(
            model_name='mpandray',
            name='vola_vina',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
