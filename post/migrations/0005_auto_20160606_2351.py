# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20160606_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]