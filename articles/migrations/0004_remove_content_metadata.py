# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_content_metadata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='metadata',
        ),
    ]
