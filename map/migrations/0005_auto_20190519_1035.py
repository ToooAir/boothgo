# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-19 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20190512_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booth',
            name='desc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
