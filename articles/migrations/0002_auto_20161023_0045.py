# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 04:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='article_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='article_title',
            field=models.CharField(default=datetime.datetime(2016, 10, 23, 4, 45, 42, 589000, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='article_author',
            field=models.TextField(max_length=2000),
        ),
    ]
