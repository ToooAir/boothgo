# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-25 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='booth',
            name='rl',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
