# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-23 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0034_auto_20171223_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processingnode',
            name='gpx',
            field=models.FileField(null=True, upload_to=b'/home/victor/Documents/Projet/poldrone/media'),
        ),
    ]
