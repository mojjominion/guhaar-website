# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20170929_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_img',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_img',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
