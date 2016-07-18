# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hat', '0029_delete_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hat.Game')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hat.UserProfile')),
            ],
        ),
    ]
