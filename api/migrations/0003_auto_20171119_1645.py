# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 16:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171119_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_link', models.CharField(max_length=200)),
                ('url_alive', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2017, 11, 19, 16, 45, 32, 968850, tzinfo=utc))),
            ],
        ),
        migrations.RemoveField(
            model_name='url',
            name='pdf',
        ),
        migrations.AlterField(
            model_name='pdffile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 19, 16, 45, 32, 968430, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='URL',
        ),
        migrations.AddField(
            model_name='pdfurl',
            name='pdf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PDFFile'),
        ),
    ]
