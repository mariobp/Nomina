# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 00:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0005_pagoincapacidad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PagoIncapacidad',
        ),
    ]
