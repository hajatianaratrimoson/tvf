# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-03-12 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etvf', '0019_remove_kristiana_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='kristiana',
            name='maty',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
