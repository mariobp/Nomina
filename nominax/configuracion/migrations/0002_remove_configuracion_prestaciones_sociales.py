# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion',
            name='prestaciones_sociales',
        ),
    ]
