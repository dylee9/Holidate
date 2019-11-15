# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-23 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hyuga_requests',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='past_hyuga',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='hyuga',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]