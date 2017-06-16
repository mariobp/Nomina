# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from recursos_h import models as recursos
# Create your models here.


class Turno(models.Model):
    empleado = models.ForeignKey(recursos.Empleado)
    fecha = models.DateField(auto_now_add=True)
    entrada = models.TimeField()
    salida = models.TimeField()
    extras = models.IntegerField("Hora extra", blank=True, null=True)
    extra_nocturna = models.IntegerField("Hora extra nocturna", blank=True, null=True)
    extra_diurna = models.IntegerField("Hora extra dierna", blank=True, null=True)
    extra_dominical = models.IntegerField("Hora extra dominical", blank=True, null=True)

    def __unicode__(self):
        return u"Turno: %s %s - %s" % (self.empleado.nombre, self.empleado.apellidos, self.fecha.strftime('%Y-%m-%d'))
    # end def
# end class
