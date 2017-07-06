# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recursos_h', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('cerrado', models.BooleanField(default=False)),
                ('nocturna', models.IntegerField(verbose_name='Valor de recargo nocturno %')),
                ('dominical', models.IntegerField(verbose_name='Valor de recargo dominical o festivo %')),
                ('nocturna_dominical', models.IntegerField(verbose_name='Valor de recargo nocturno dominical o festivo %')),
                ('descuento_salud', models.IntegerField(verbose_name='Descuento de salud y pensi\xf3n para empleado %')),
                ('prestaciones_sociales', models.IntegerField(verbose_name='Pago de salud y pensi\xf3n del empleador %')),
                ('extra_diurna', models.IntegerField(verbose_name='Valor de recargo de hora extra diurna %')),
                ('extra_nocturna', models.IntegerField(verbose_name='Valor de recargo de hora extra nocturna %')),
                ('extra_dominical_diurna', models.IntegerField(verbose_name='Valor de recargo de hora extra dominical %')),
                ('extra_dominical_nocturna', models.IntegerField(verbose_name='Valor de recargo de hora extra dominical nocturna %')),
            ],
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio_mes', models.DateField(blank=True, null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('salario_base', models.FloatField(max_length=100)),
                ('subsidio_trasporte', models.FloatField(blank=True, max_length=100, null=True)),
                ('diurnas', models.FloatField(blank=True, null=True, verbose_name='Hora diurna')),
                ('nocturna', models.FloatField(blank=True, null=True, verbose_name='Hora nocturna')),
                ('dominical_diurna', models.FloatField(blank=True, null=True, verbose_name='Hora dominical diurna')),
                ('dominical_nocturna', models.FloatField(blank=True, null=True, verbose_name='Hora dominical nocturna')),
                ('extras', models.FloatField(blank=True, null=True, verbose_name='Hora extra diurna')),
                ('extra_nocturna', models.FloatField(blank=True, null=True, verbose_name='Hora extra nocturna')),
                ('extra_dominical_diurna', models.FloatField(blank=True, null=True, verbose_name='Hora extra dominical diurna')),
                ('extra_dominical_nocturna', models.FloatField(blank=True, null=True, verbose_name='Hora extra dominical nocturna')),
                ('corte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.Corte')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos_h.Empleado')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='nomina',
            unique_together=set([('empleado', 'corte')]),
        ),
    ]
