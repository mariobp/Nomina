# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from recursos_h import models as recursos


class Corte(models.Model):
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(blank=True, null=True)
    cerrado = models.BooleanField(default=False)

    @staticmethod
    def get_instance():
        return Corte.objects.filter(cerrado=False).order_by('fecha_fin').last()
    # end def
# enc class


class Nomina(models.Model):
    empleado = models.ForeignKey(recursos.Empleado)
    corte = models.ForeignKey(Corte)
    fecha = models.DateField(auto_now_add=True)
    salario_base = models.CharField(max_length=100)
    subsidio_trasporte = models.CharField(max_length=100)
    extras = models.IntegerField("Hora extra", blank=True, null=True)
    extra_nocturna = models.IntegerField("Hora extra nocturna", blank=True, null=True)
    extra_diurna = models.IntegerField("Hora extra dierna", blank=True, null=True)
    extra_dominical = models.IntegerField("Hora extra dominical", blank=True, null=True)
    prestaciones_sociales = models.CharField(max_length=100)
    salario_produccion = models.CharField(max_length=100)
    bonificacion = models.CharField(max_length=100)

    class Meta:
        unique_together = ('empleado', 'corte')
    # end class

    def __unicode__(self):
        return u"Nomina %s %s - %s" % (self.empleado.nombre, self.empleado.apellidos, self.fecha.strftime('%Y-%m-%d'))
    # end def
# end class
