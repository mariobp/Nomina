# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0009_auto_20170701_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomina',
            name='bonificacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nomina',
            name='prestaciones_sociales',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nomina',
            name='salario_produccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nomina',
            name='subsidio_trasporte',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
