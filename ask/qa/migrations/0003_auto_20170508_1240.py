# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20170506_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(blank=True),
        ),
    ]
