# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20161029_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]