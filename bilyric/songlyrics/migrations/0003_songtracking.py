# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-09 13:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songlyrics', '0002_song_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongTracking',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songlyrics.Song')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]