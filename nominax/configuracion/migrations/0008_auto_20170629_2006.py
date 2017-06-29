# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0007_auto_20170628_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='extra_diurna',
            field=models.IntegerField(default=1, verbose_name='Valor hora extra diurna'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracion',
            name='extra_dominical',
            field=models.IntegerField(default=1, verbose_name='Valor hora extra dominical'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracion',
            name='extra_dominical_nocturna',
            field=models.IntegerField(default=1, verbose_name='Valor hora extra dominical nocturna'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracion',
            name='extra_nocturna',
            field=models.IntegerField(default=1, verbose_name='Valor hora extra nocturna'),
            preserve_default=False,
        ),
    ]
