# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hat', '0009_room_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_creation', models.DateTimeField(verbose_name='Time of room creation')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hat.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Secret_word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hat.Game')),
            ],
        ),
    ]
