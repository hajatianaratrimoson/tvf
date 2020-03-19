# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-03-05 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etvf', '0002_remove_mpikambana_mpandray'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toerana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anarana_toerana', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='mpikambana',
            name='toerana_mpikambana',
        ),
        migrations.RemoveField(
            model_name='tossaafi',
            name='mpandray',
        ),
        migrations.RemoveField(
            model_name='tossaafi',
            name='toerana',
        ),
        migrations.AddField(
            model_name='mpikambana',
            name='mpandray',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='etvf.Mpandray'),
        ),
        migrations.AddField(
            model_name='mpikambana',
            name='tossaafi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='etvf.Tossaafi'),
        ),
        migrations.AlterField(
            model_name='tossaafi',
            name='anarana_tossaafi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mpikambana',
            name='toerana',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='etvf.Toerana'),
        ),
    ]