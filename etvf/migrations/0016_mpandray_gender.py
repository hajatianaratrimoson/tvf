# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-03-10 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etvf', '0015_tossaafi_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpandray',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]