# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-03-10 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etvf', '0012_auto_20200309_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laminasa',
            name='daty_laminasa',
            field=models.DateField(),
        ),
    ]
