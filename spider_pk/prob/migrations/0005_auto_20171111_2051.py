# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prob', '0004_probtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProbTotals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probtotal_rule', models.CharField(max_length=100)),
                ('probtotal_match', models.IntegerField()),
                ('probtotal_nomatch', models.IntegerField()),
                ('probtotal_bet', models.IntegerField()),
                ('probtotal_amount', models.FloatField()),
                ('probtotal_win', models.FloatField()),
                ('probtotal_lose', models.FloatField()),
                ('probtotal_gain', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='ProbTotal',
        ),
    ]
