# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
