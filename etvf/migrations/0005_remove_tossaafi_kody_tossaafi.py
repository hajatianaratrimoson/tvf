# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-03-05 08:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etvf', '0004_tossaafi_kody_tossaafi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tossaafi',
            name='kody_tossaafi',
        ),
    ]