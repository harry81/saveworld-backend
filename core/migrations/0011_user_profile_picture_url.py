# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-16 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20161230_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture_url',
            field=models.CharField(blank=True, default=True, max_length=512, null=True),
        ),
    ]
