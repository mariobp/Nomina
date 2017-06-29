# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from recursos_h import models as recursos
from cuser.fields import CurrentUserField
from django.contrib.auth.models import User
from datedelta import datedelta, multi_datedelta, periodic_timedelta
from datetime import date, timedelta, time

class RangoFecha(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    @staticmethod
    def create(fecha_inicio, fecha_fin):
        rango = RangoFecha()
        rango.fecha_inicio = fecha_inicio
        rango.fecha_fin = fecha_fin
        rango.save()
        return rango
    # end def

    def __unicode__(self):
        return "[%s - %s]" % (str(self.fecha_inicio), str(self.fecha_fin))
    # end def

# end class

class Turno(models.Model):
    empleado = models.ForeignKey(recursos.Empleado)
    entrada = models.DateTimeField()
    salida = models.DateTimeField()
    
    extras = models.ManyToManyField(RangoFecha, related_name='extras', blank=True)
    nocturna = models.ManyToManyField(RangoFecha, related_name='nocturna', blank=True)
    diurna = models.ManyToManyField(RangoFecha, related_name='diurna', blank=True)
    dominical = models.ManyToManyField(RangoFecha, related_name='dominical', blank=True)

    aprobado = models.BooleanField(default=False)
    aprobado_user = models.ForeignKey(User, verbose_name="Usuario que aprobo el turno", blank=True, null=True)
    creator = CurrentUserField(add_only=True, related_name="created_turno")
    last_editor = CurrentUserField(related_name="last_edited_turno")

    def horas_extras(self):
        return self.extras

    def __unicode__(self):
        return u"Turno: %s %s - %s" % (self.empleado.nombre, self.empleado.apellidos, self.entrada.strftime('%Y-%m-%d'))
    # end def
# end class

class DiaFestivo(models.Model):
    choices = (
        (1, 'Enero'),
        (2, 'Febrero'),
        (3, 'Marzo'),
        (4, 'Abril'),
        (5, 'Mayo'),
        (6, 'Junio'),
        (7, 'Julio'),
        (8, 'Agosto'),
        (9, 'Septiembre'),
        (10, 'Octubre'),
        (11, 'Noviembre'),
        (12, 'Diciembre'),
    )
    dia = models.IntegerField("Día")
    mes = models.IntegerField(choices=choices)

    @staticmethod
    def multi_datedelta(date_delta):
        dias = DiaFestivo.objects.filter(dia__gte=date_delta.start_date.day, dia__lte=date_delta.end_date.day, mes__gte=date_delta.start_date.month, mes__lte=date_delta.end_date.month)
        date_deltas = []
        for dia in dias:
            delta = datedelta.for_day(date(date_delta.start_date.year, dia.dia, dia.mes), time(0, 0, 0), time(23, 59, 59))
            date_deltas.append(delta)
        # end for
        return multi_datedelta(date_deltas)
    # end def

# end class

class DiaDominical(models.Model):
    choices = (
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    )
    dia = models.IntegerField("Día", choices=choices)

    @staticmethod
    def multi_datedelta(date_delta):
        dias = DiaDominical.objects.all()
        date_deltas = []
        for dia in dias:
            for single_date in date_delta.daterange():
                if single_date.weekday() == dia.dia:
                    delta = datedelta.for_day(single_date, time(0, 0, 0), time(23, 59, 59))
                    date_deltas.append(delta)
                # end if
            # end for
        # end for
        return multi_datedelta(date_deltas)
    # end def

    def proximo(self):
        dia = date.today()
        while (dia.weekday() != self.dia):
            dia = dia + timedelta(days=1)
        # end while
        return dia
    # end def

    def anterior(self):
        dia = date.today()
        while (dia.weekday() != self.dia):
            dia = dia - timedelta(days=1)
        # end while
        return dia
    # end def

    def __unicode__(self):
        return "%s, el %d° día de la semana" % (dict(self.choices)[self.dia], self.dia)
    # end def

# end class