# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-15 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songlyrics', '0003_songtracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='songtracking',
            name='ip_address',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
    ]