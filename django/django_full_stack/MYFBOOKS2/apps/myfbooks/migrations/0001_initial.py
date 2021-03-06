# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-27 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0002_auto_20190822_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=600)),
                ('likes', models.ManyToManyField(related_name='liked_books', to='login_app.MyUser')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_uploded', to='login_app.MyUser')),
            ],
        ),
    ]
