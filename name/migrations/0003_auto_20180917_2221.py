# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-17 22:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0002_change_choice_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'base_manager_name': 'objects', 'ordering': ['status']},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'base_manager_name': 'objects'},
        ),
    ]
