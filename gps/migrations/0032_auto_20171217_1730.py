# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-17 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0031_auto_20171217_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processingnode',
            name='pollution',
            field=models.FileField(default='/home/victor/Documents/Projet/poldrone/media/Vol.gpx', upload_to=b'/home/victor/Documents/Projet/poldrone/media'),
        ),
    ]
