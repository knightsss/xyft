# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-12 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProbUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=30)),
                ('user_password', models.CharField(max_length=30)),
                ('user_status', models.BooleanField()),
            ],
        ),
    ]
