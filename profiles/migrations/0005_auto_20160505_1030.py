# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20160504_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promise',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Promise',
        ),
    ]
