# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 04:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
