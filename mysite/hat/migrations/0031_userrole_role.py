# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hat', '0030_userrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrole',
            name='role',
            field=models.CharField(choices=[('LID', 'Lider'), ('PL', 'Player')], default='LID', max_length=3),
        ),
    ]
