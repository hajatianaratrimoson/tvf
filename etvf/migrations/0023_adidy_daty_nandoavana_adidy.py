# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-03-13 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etvf', '0022_kitapo_daty_nadoavana_kitapo'),
    ]

    operations = [
        migrations.AddField(
            model_name='adidy',
            name='daty_nandoavana_adidy',
            field=models.DateField(blank=True, null=True),
        ),
    ]
