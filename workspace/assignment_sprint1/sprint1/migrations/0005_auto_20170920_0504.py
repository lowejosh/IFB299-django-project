# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint1', '0004_auto_20170920_0442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='imageDirectory',
            new_name='imagePath',
        ),
        migrations.AddField(
            model_name='location',
            name='locationImagePath',
            field=models.CharField(max_length=127, null=True),
        ),
    ]
