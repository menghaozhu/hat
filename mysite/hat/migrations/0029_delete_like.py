# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 12:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hat', '0028_auto_20160407_1943'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]