# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_h', '0005_auto_20170630_1808'),
        ('nomina', '0003_auto_20170622_2125'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nomina',
            unique_together=set([('empleado', 'corte')]),
        ),
    ]
