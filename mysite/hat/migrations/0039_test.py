# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hat', '0038_auto_20160510_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hello', models.IntegerField(default=0)),
                ('name', models.CharField(default='Vasya', max_length=20)),
            ],
        ),
    ]
