# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0021_land_share_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='share_amount_percentage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
