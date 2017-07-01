# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0009_auto_20170629_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion',
            name='extra_dominical',
        ),
        migrations.AddField(
            model_name='configuracion',
            name='dominical',
            field=models.IntegerField(default=1, verbose_name='Valor de recargo dominical o festivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracion',
            name='extra_dominical_diurna',
            field=models.IntegerField(default=1, verbose_name='Valor de recargo de hora extra dominical'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracion',
            name='nocturna',
            field=models.IntegerField(default=1, verbose_name='Valor de recargo nocturno'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='extra_diurna',
            field=models.IntegerField(verbose_name='Valor de recargo de hora extra diurna'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='extra_dominical_nocturna',
            field=models.IntegerField(verbose_name='Valor de recargo de hora extra dominical nocturna'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='extra_nocturna',
            field=models.IntegerField(verbose_name='Valor de recargo de hora extra nocturna'),
        ),
    ]
