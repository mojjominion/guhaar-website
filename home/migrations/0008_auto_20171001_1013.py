# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_member_team'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
