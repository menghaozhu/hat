# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hat', '0032_auto_20160510_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hat.Game'),
        ),
    ]
