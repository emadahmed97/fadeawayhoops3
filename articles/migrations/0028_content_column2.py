# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 03:06
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0027_auto_20161031_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='column2',
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
    ]
