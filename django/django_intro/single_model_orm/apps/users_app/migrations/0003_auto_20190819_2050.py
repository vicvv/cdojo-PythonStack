# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-19 20:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20190819_1930'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]