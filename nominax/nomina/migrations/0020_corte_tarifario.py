# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_h', '0012_auto_20170707_1824'),
        ('nomina', '0019_auto_20170706_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='corte',
            name='tarifario',
            field=models.ManyToManyField(to='recursos_h.Tarifario'),
        ),
    ]
