# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_person_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='qualification',
            field=models.CharField(max_length=250, null=True),
        ),
    ]