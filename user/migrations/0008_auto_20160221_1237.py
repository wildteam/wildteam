# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20160221_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tel',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=60),
        ),
    ]