# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cuser.fields import CurrentUserField
from django.contrib.auth.models import User
from datetime import date


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    valor_hora_diurna = models.DecimalField(max_digits=10, decimal_places=2)
    valor_hora_nocturna = models.DecimalField(max_digits=10, decimal_places=2)
    creator = CurrentUserField(add_only=True, related_name="created_cargo")
    last_editor = CurrentUserField(related_name="last_edited_cargo")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_cargo", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Pension(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, blank=True, null=True)
    creator = CurrentUserField(add_only=True, related_name="created_pension")
    last_editor = CurrentUserField(related_name="last_edited_pension")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_pension", blank=True, null=True)

    class Meta:
        verbose_name = "Pensión"
        verbose_name_plural = "Pensiones"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Eps(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, blank=True, null=True)
    creator = CurrentUserField(add_only=True, related_name="created_eps")
    last_editor = CurrentUserField(related_name="last_edited_eps")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_eps", blank=True, null=True)

    class Meta:
        verbose_name = "Eps"
        verbose_name_plural = "Eps"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Cesantia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, blank=True, null=True)
    creator = CurrentUserField(add_only=True, related_name="created_cesantia")
    last_editor = CurrentUserField(related_name="last_edited_cesantia")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_cesantia", blank=True, null=True)

    class Meta:
        verbose_name = "Cesantía"
        verbose_name_plural = "Cesantías"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class CajaCompensacion(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, blank=True, null=True)
    creator = CurrentUserField(add_only=True, related_name="created_caja")
    last_editor = CurrentUserField(related_name="last_edited_caja")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_caja", blank=True, null=True)

    class Meta:
        verbose_name = "Caja de compensación"
        verbose_name_plural = "Cajas de compencación"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    cedula = models.CharField(max_length=100, unique=True)
    fecha_nacimiento = models.DateField()
    cargo = models.ForeignKey(Cargo)
    pension = models.ForeignKey(Pension)
    eps = models.ForeignKey(Eps)
    cesantia = models.ForeignKey(Cesantia)
    cajacompensacion = models.ForeignKey(CajaCompensacion)
    creator = CurrentUserField(add_only=True, related_name="created_empleado")
    last_editor = CurrentUserField(related_name="last_edited_empleado")

    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.apellidos)
    # end def
# end class


class TipoContrato(models.Model):
    opciones = (
        (1, 'Por hora'),
        (2, 'Salario fijo')
    )
    nombre = models.CharField(max_length=100)
    modalidad = models.IntegerField(choices=opciones)
    creator = CurrentUserField(add_only=True, related_name="created_tipo_contrato")
    last_editor = CurrentUserField(related_name="last_edited_tipo_contrato")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_tipo_contrato", blank=True, null=True)

    class Meta:
        verbose_name = "Tipo de contrato"
        verbose_name_plural = "Tipos de contrato"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Contrato(models.Model):
    empleado = models.ForeignKey(Empleado)
    tipo_contrato = models.ForeignKey(TipoContrato)
    salario_base = models.CharField("Salario base legal", max_length=100)

    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField(blank=True, null=True)

    descanso_turno = models.BooleanField("Descanso entre turnos")
    inicio_descanso = models.IntegerField("Hora de inicio de descanso", blank=True, null=True)
    duracion_descanso = models.IntegerField("Duración de descanso en minutos", blank=True, null=True)
    horas_trabajo = models.IntegerField("Horas de trabajo", default=8)

    creator = CurrentUserField(add_only=True, related_name="created_contrato")
    last_editor = CurrentUserField(related_name="last_edited_contrato")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_contrato", blank=True, null=True)

    @staticmethod
    def get_instance(empleado):
        return Contrato.objects.filter(empleado=empleado).exclude(fecha_finalizacion__lte=date.today()).order_by('fecha_inicio').last()
    # end def

    def __unicode__(self):
        return u"Contrato de %s %s" % (self.empleado.nombre, self.empleado.apellidos)
    # end def
# end class|
