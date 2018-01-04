# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-04 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0039_auto_20180103_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processingnode',
            name='gpx',
            field=models.FileField(null=True, upload_to='gpx/'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='pollution',
            field=models.FileField(null=True, upload_to='pollution/'),
        ),
    ]
