# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-05 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accesscodes', '0006_auto_20160705_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('short_description', models.CharField(max_length=10, unique=True)),
                ('long_description', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('event_begin', models.DateTimeField(blank=True, null=True, verbose_name='valid from')),
                ('event_end', models.DateTimeField(blank=True, null=True, verbose_name='valid from')),
            ],
        ),
        migrations.RenameField(
            model_name='code',
            old_name='type',
            new_name='code_type',
        ),
    ]
