# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hat', '0019_auto_20160325_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='users',
        ),
    ]
