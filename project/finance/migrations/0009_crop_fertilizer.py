# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_land_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.CharField(max_length=50)),
                ('unit_price', models.IntegerField()),
                ('amount_per_sqft', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizer_name', models.CharField(max_length=50)),
                ('unit_price', models.IntegerField()),
                ('amount_per_sqft', models.DecimalField(decimal_places=2, max_digits=20)),
                ('crop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Crop')),
            ],
        ),
    ]
