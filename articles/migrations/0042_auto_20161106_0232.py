# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0041_content_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
