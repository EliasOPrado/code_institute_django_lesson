# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-23 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='done',
        ),
    ]
