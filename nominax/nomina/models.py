# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from recursos_h import models as recursos
# Create your models here.


class Nomina(models.Model):
    empleado = models.ForeignKey(recursos.Empleado)
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

    def __unicode__(self):
        return u"Nomina %s %s - %s" % (self.empleado.nombre, self.empleado.apellidos, self.fecha.strftime('%Y-%m-%d'))
    # end def
# end class
