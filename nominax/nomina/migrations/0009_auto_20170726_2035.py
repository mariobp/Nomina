# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 20:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nomina', '0008_descuento_corte_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaincapacidad',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='diaincapacidad',
            name='eliminado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eliminado_por_dia_incapacidad', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagoincapacidad',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pagoincapacidad',
            name='eliminado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eliminado_por_pago_incapacidad', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tipoincapacidad',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tipoincapacidad',
            name='eliminado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eliminado_por_tipo_incapacidad', to=settings.AUTH_USER_MODEL),
        ),
    ]
