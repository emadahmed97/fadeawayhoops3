# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20161024_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='article_text',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='article_title',
            field=models.CharField(max_length=200),
        ),
    ]
