# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='land',
        ),
    ]
