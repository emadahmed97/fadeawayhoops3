# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 20:26
from __future__ import unicode_literals

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20161024_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to=articles.models.get_image_path),
        ),
    ]
