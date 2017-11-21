# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 16:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDFFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2017, 11, 19, 16, 38, 55, 808413))),
            ],
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_link', models.CharField(max_length=200)),
                ('url_alive', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2017, 11, 19, 16, 38, 55, 808830))),
                ('pdf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PDFFile')),
            ],
        ),
    ]
