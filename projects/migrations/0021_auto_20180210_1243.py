# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_interview_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interview',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ['-date_created']},
        ),
        migrations.RenameField(
            model_name='story',
            old_name='date_started',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='interview',
            name='date_created',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='video',
            name='date_created',
            field=models.DateTimeField(default=None),
        ),
    ]
