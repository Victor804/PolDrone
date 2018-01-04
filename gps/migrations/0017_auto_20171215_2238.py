# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-15 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0016_auto_20171215_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processingnode',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='Date'),
        ),
    ]
