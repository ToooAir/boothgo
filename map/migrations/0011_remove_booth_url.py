# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-27 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_merge_20190525_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booth',
            name='url',
        ),
    ]
