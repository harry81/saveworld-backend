# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-15 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_item_fb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='core_item_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
