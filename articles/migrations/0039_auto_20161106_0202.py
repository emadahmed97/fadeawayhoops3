# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0038_auto_20161101_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='heading16',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='heading17',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='paragraph16',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='paragraph17',
            field=models.TextField(max_length=20000, null=True),
        ),
    ]