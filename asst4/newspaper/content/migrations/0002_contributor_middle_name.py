# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='middle_name',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
