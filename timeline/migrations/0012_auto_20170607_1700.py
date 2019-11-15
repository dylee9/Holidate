# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-07 08:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0011_auto_20170607_1659'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'Employee'},
        ),
        migrations.AlterModelOptions(
            name='hyuga_confirmed',
            options={'verbose_name_plural': 'Confirmed Break List'},
        ),
        migrations.AlterModelOptions(
            name='hyuga_requests',
            options={'verbose_name_plural': 'Requested Break List'},
        ),
        migrations.AlterModelOptions(
            name='past_hyuga',
            options={'verbose_name_plural': 'Past Break List'},
        ),
    ]