# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-23 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hPlay', '0003_auto_20161023_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Nepali', 'Nepali'), ('Hindi', 'Hindi'), ('Dzongkha', 'Dzongkha')], default='English', max_length=10),
        ),
        migrations.AddField(
            model_name='playlist',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Nepali', 'Nepali'), ('Hindi', 'Hindi'), ('Dzongkha', 'Dzongkha')], default='English', max_length=10),
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('Movie', 'Movie'), ('Pop', 'Pop'), ('Rock', 'Rock'), ('Remix', 'Remix'), ('Instrumental', 'Instrumental'), ('Folk', 'Folk'), ('Electronic', 'Electronic')], default='Unknown', max_length=15),
        ),
    ]
