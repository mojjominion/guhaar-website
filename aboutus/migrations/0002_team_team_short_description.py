# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_short_description',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
