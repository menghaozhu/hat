# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hat', '0033_auto_20160510_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user_role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hat.UserRole'),
        ),
    ]