# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-13 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_topic_view'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='view',
            new_name='views',
        ),
    ]
