# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Pension(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, blank=True, null=True)

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
    cargo = models.ForeignKey(Cargo)
    pension = models.ForeignKey(Pension)
    eps = models.ForeignKey(Eps)
    cesantia = models.ForeignKey(Cesantia)
    cajacompensacion = models.ForeignKey(CajaCompensacion)

    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.apellidos)
    # end def
# end class


class TipoContrato(models.Model):
    nombre = models.CharField(max_length=100)
    extra_diurna = models.FloatField("Hora extra diurna")
    extra_nocturna = models.FloatField("Hora extra nocturna")
    extra_dominical = models.FloatField("Hora extra dominical")
    extra_dominical_nocturna = models.CharField("Hora extra dominical nocturna")

    class Meta:
        verbose_name = "Tipo de contrato"
        verbose_name_plural = "Tipos de contrato"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Contrato(models.Model):
    empleado = models.OneToOneField(Empleado)
    fecha_inicio = models.DateField()
    salario_base = models.CharField("Salario base legal", max_length=100)
    tipo_contrato = models.ForeignKey(TipoContrato)
    descanso_turno = models.BooleanField("Descanso entre turnos")
    inicio_descanso = models.IntegerField("Hora de inicio de descanso", blank=True, null=True)
    duracion_descanso = models.IntegerField("Duración de descanso en minutos", blank=True, null=True)

    def __unicode__(self):
        return u"Contrato de %s %s" % (self.empleado.nombre, self.empleado.apellidos)
    # end def
# end class|
