# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0032_remove_content_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='heading1',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='heading2',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='heading3',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='heading4',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='heading5',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='paragraph1',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='paragraph2',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='paragraph3',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='paragraph4',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='paragraph5',
            field=models.TextField(max_length=20000, null=True),
        ),
    ]