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

    def datedelta(self):
        return datedelta(self.fecha_inicio, self.fecha_fin)
    # end def

    def horas(self):
        return datedelta(self.fecha_inicio, self.fecha_fin).horas()
    # end def

    def __unicode__(self):
        return "[%s - %s]" % (str(self.fecha_inicio), str(self.fecha_fin))
    # end def

# end class

class Turno(models.Model):
    empleado = models.ForeignKey(recursos.Empleado)
    entrada = models.DateTimeField()
    salida = models.DateTimeField(null=True, blank=True)

    extras = models.ManyToManyField(RangoFecha, related_name='extras', blank=True)
    nocturna = models.ManyToManyField(RangoFecha, related_name='nocturna', blank=True)
    diurna = models.ManyToManyField(RangoFecha, related_name='diurna', blank=True)
    dominical = models.ManyToManyField(RangoFecha, related_name='dominical', blank=True)

    aprobado = models.BooleanField(default=False)
    aprobado_user = models.ForeignKey(User, verbose_name="Usuario que aprobo el turno", blank=True, null=True)
    creator = CurrentUserField(add_only=True, related_name="created_turno")
    last_editor = CurrentUserField(related_name="last_edited_turno")

    @staticmethod
    def month(empleado, year, month):
        return Turno.objects.filter(empleado=empleado, entrada__year=year, salida__month=month)
    # end def

    def get_extras_nocturnas(self):
        delta_extras = self.get_delta_extras()
        delta_nocturna = self.get_delta_nocturna()
        return delta_extras.intersect(delta_nocturna).horas()
    # end def

    def get_extras_diurnas(self):
        delta_extras = self.get_delta_extras()
        delta_diurna = self.get_delta_diurna()
        return delta_extras.intersect(delta_diurna).horas()
    # end def

    def get_dominicales_nocturnas(self):
        delta_dominical = self.get_delta_dominical()
        delta_nocturna = self.get_delta_nocturna()
        return delta_dominical.intersect(delta_nocturna).horas()
    # end def

    def get_dominicales_diurnas(self):
        delta_dominical = self.get_delta_dominical()
        delta_diurna = self.get_delta_diurna()
        return delta_dominical.intersect(delta_diurna).horas()
    # end def

    def get_dominicales_nocturnas_extra(self):
        delta_dominical = self.get_delta_dominical()
        delta_nocturna = self.get_delta_nocturna()
        delta_extras = self.get_delta_extras()
        return delta_dominical.intersect(delta_nocturna).intersect(delta_extras).horas()
    # end def

    def get_dominicales_diurnas_extra(self):
        delta_dominical = self.get_delta_dominical()
        delta_diurna = self.get_delta_diurna()
        delta_extras = self.get_delta_extras()
        return delta_dominical.intersect(delta_diurna).intersect(delta_extras).horas()
    # end def

    def get_delta_extras(self):
        delta = multi_datedelta()
        for rango in self.extras.all():
            delta = delta + rango.datedelta()
        # end for
        return delta
    # end def

    def get_delta_nocturna(self):
        delta = multi_datedelta()
        for rango in self.nocturna.all():
            delta = delta + rango.datedelta()
        # end for
        return delta
    # end def

    def get_delta_diurna(self):
        delta = multi_datedelta()
        for rango in self.diurna.all():
            delta = delta + rango.datedelta()
        # end for
        return delta
    # end def

    def get_delta_dominical(self):
        delta = multi_datedelta()
        for rango in self.dominical.all():
            delta = delta + rango.datedelta()
        # end for
        return delta
    # end def

    def horas_extras(self):
        horas = 0
        for rango in self.extras.all():
            horas = horas + rango.horas()
        # end for
        return horas if horas > 0 else 0
    # end def

    def horas_nocturna(self):
        horas = 0
        for rango in self.nocturna.all():
            horas = horas + rango.horas()
        # end for
        return horas
    # end def

    def horas_diurna(self):
        horas = 0
        for rango in self.diurna.all():
            horas = horas + rango.horas()
        # end for
        return horas
    # end def

    def total_horas(self):
        return self.horas_diurna() + self.horas_nocturna()
    # end def

    def horas_dominical(self):
        horas = 0
        for rango in self.dominical.all():
            horas = horas + rango.horas()
        # end for
        return horas
    # end def

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
            single_date = date(date_delta.start_date.year, dia.mes, dia.dia)
            delta = datedelta.for_day(single_date, datedelta.START_TIME, datedelta.END_TIME)
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
                    delta = datedelta.for_day(single_date, datedelta.START_TIME, datedelta.END_TIME)
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

class Produccion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    unidad = models.ForeignKey(recursos.UnidadProduccion)
    cantidad = models.IntegerField()
    empleados = models.ManyToManyField(recursos.Empleado)

    creator = CurrentUserField(add_only=True, related_name="created_produccion")
    last_editor = CurrentUserField(related_name="last_edited_produccion")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_produccion", blank=True, null=True)

# end class