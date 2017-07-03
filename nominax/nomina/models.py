# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from recursos_h import models as recursos


class Corte(models.Model):
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(blank=True, null=True)
    cerrado = models.BooleanField(default=False)

    nocturna = models.IntegerField("Valor de recargo nocturno %")
    dominical = models.IntegerField("Valor de recargo dominical o festivo %")
    nocturna_dominical = models.IntegerField("Valor de recargo nocturno dominical o festivo %")
    
    extra_diurna = models.IntegerField("Valor de recargo de hora extra diurna %")
    extra_nocturna = models.IntegerField("Valor de recargo de hora extra nocturna %")

    extra_dominical_diurna = models.IntegerField("Valor de recargo de hora extra dominical %")
    extra_dominical_nocturna = models.IntegerField("Valor de recargo de hora extra dominical nocturna %")


    @staticmethod
    def get_instance():
        return Corte.objects.filter(cerrado=False).order_by('fecha_inicio').last()
    # end def
# enc class


class Nomina(models.Model):
    empleado = models.ForeignKey(recursos.Empleado)
    corte = models.ForeignKey(Corte)
    fecha = models.DateField(auto_now_add=True)
    salario_base = models.FloatField(max_length=100)
    subsidio_trasporte = models.CharField(max_length=100)
    
    extras = models.FloatField("Hora extra", blank=True, null=True)
    extra_nocturna = models.FloatField("Hora extra nocturna", blank=True, null=True)
    extra_dominical_diurna = models.FloatField("Hora extra dominical diurna", blank=True, null=True)
    extra_dominical_nocturna = models.FloatField("Hora extra dominical nocturna", blank=True, null=True)
    dominical_diurna = models.FloatField("Hora dominical diurna", blank=True, null=True)
    dominical_nocturna = models.FloatField("Hora dominical nocturna", blank=True, null=True)
    nocturna = models.FloatField("Hora nocturna", blank=True, null=True)

    prestaciones_sociales = models.CharField(max_length=100)
    salario_produccion = models.CharField(max_length=100)
    bonificacion = models.CharField(max_length=100)

    def valor_hora(self):
        return self.salario_base/240
    # end def

    def calcular_hora_extra_diurna(self):
        valor_hora = self.valor_hora()
        return str(valor_hora*self.corte.extra_diurna/100*self.extras)
    # end def

    def calcular_hora_nocturna(self):
        valor_hora = self.valor_hora()
        return str(valor_hora*self.corte.nocturna/100*self.nocturna)
    # end def

    def calcular_hora_extra_nocturna(self):
        valor_hora = self.valor_hora()
        return str(valor_hora*self.corte.extra_nocturna/100*self.extra_nocturna)
    # end def

    def calcular_hora_dominical_diurna(self):
        valor_hora = self.valor_hora()
        return str(valor_hora*self.corte.dominical/100*self.dominical_diurna)
    # end def

    def calcular_hora_dominical_nocturna(self):
        valor_hora = self.valor_hora()
        return str(valor_hora*self.corte.nocturna_dominical/100*self.dominical_nocturna)
    # end def

    def calcular_hora_dominical_extra_diurna(self):
        valor_hora = self.valor_hora()
        return str(valor_hora*self.corte.extra_dominical_diurna/100*self.extra_dominical_diurna)
    # end def

    def calcular_hora_dominical_extra_nocturna(self):
        valor_hora = self.valor_hora()
        return str(valor_hora*self.corte.extra_dominical_nocturna/100*self.extra_dominical_nocturna)
    # end def

    class Meta:
        unique_together = ('empleado', 'corte')
    # end class

    def __unicode__(self):
        return u"Nomina %s %s - %s" % (self.empleado.nombre, self.empleado.apellidos, self.fecha.strftime('%Y-%m-%d'))
    # end def
# end class
