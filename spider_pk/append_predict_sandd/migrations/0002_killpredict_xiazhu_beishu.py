# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-22 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('append_predict_sandd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='killpredict',
            name='xiazhu_beishu',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
