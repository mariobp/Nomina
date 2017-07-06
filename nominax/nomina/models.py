# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from recursos_h import models as recursos
from datetime import date, timedelta
from turno.datedelta import datedelta, multi_datedelta
from turno import models as turno


class Corte(models.Model):
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(blank=True, null=True)
    cerrado = models.BooleanField(default=False)

    nocturna = models.IntegerField("Valor de recargo nocturno %")
    dominical = models.IntegerField("Valor de recargo dominical o festivo %")
    nocturna_dominical = models.IntegerField("Valor de recargo nocturno dominical o festivo %")
    descuento_salud = models.IntegerField("Descuento de salud y pensión para empleado %")
    prestaciones_sociales = models.IntegerField("Pago de salud y pensión del empleador %")

    extra_diurna = models.IntegerField("Valor de recargo de hora extra diurna %")
    extra_nocturna = models.IntegerField("Valor de recargo de hora extra nocturna %")

    extra_dominical_diurna = models.IntegerField("Valor de recargo de hora extra dominical %")
    extra_dominical_nocturna = models.IntegerField("Valor de recargo de hora extra dominical nocturna %")


    @staticmethod
    def get_instance():
        return Corte.objects.filter(cerrado=False).order_by('fecha_inicio').last()
    # end def
# end class

class Nomina(models.Model):
    inicio_mes = models.DateField(blank=True, null=True)

    empleado = models.ForeignKey(recursos.Empleado)
    corte = models.ForeignKey(Corte)
    fecha = models.DateField(auto_now_add=True)
    salario_base = models.FloatField(max_length=100)
    subsidio_trasporte = models.FloatField(max_length=100, blank=True, null=True)

    diurnas = models.FloatField("Hora diurna", blank=True, null=True)
    nocturna = models.FloatField("Hora nocturna", blank=True, null=True)
    dominical_diurna = models.FloatField("Hora dominical diurna", blank=True, null=True)
    dominical_nocturna = models.FloatField("Hora dominical nocturna", blank=True, null=True)
    
    extras = models.FloatField("Hora extra diurna", blank=True, null=True)
    extra_nocturna = models.FloatField("Hora extra nocturna", blank=True, null=True)
    extra_dominical_diurna = models.FloatField("Hora extra dominical diurna", blank=True, null=True)
    extra_dominical_nocturna = models.FloatField("Hora extra dominical nocturna", blank=True, null=True)

    def salario_produccion(self):
        if False and self.horas_diurna and self.horas_nocturna and self.horas_dominicales:
            return self.horas_diurna*float(self.empleado.cargo.valor_hora_diurna) + self.horas_nocturna*float(self.empleado.cargo.valor_hora_nocturna) + self.horas_dominicales*float(self.empleado.cargo.valor_hora_festivo)
        # end if
        return 0
    # end def


    def prestaciones_sociales(self):
        return self.salario_legal()*self.corte.prestaciones_sociales/100
    # end def

    def descuento_salud(self):
        return (self.salario_legal() - (self.subsidio_trasporte or 0))*self.corte.descuento_salud/100
    # end def

    def bonificacion(self):
        bonificacion = self.salario_produccion() - self.salario_legal()
        if bonificacion < 0:
            return 0
        # end if
        return bonificacion
    # end def

    def valor_hora(self):
        if self.salario_base:
            return self.salario_base/240
        # end def
        return 0
    # end def

    def salario_legal(self):
        return (self.salario_base or 0) + (self.subsidio_trasporte or 0) + self.recargos()
    # end def

    def neto(self):
        if self.salario_produccion() < self.salario_base or 0:
            return (self.salario_base or 0) + self.recargos() + (self.subsidio_trasporte or 0)
        # end if
        return self.salario_produccion()
    # end def

    def total(self):
        return self.neto() - self.descuento_salud()
    # end def

    def recargos(self):
        recargos = 0
        recargos = recargos + self.calcular_hora_extra_diurna()
        recargos = recargos + self.calcular_hora_nocturna()
        recargos = recargos + self.calcular_hora_extra_nocturna()
        recargos = recargos + self.calcular_hora_dominical_diurna()
        recargos = recargos + self.calcular_hora_dominical_nocturna()
        recargos = recargos + self.calcular_hora_dominical_extra_diurna()
        recargos = recargos + self.calcular_hora_dominical_extra_nocturna()
        return recargos
    # end def

    def calcular_hora_diurna(self):
        valor_hora = self.valor_hora()
        if self.diurnas != None:
            return int(valor_hora*self.diurnas*10**2)/10.0**2
        # end if
        return 0
    # end def

    def calcular_hora_extra_diurna(self):
        valor_hora = self.valor_hora()
        if self.extras != None:
            return int(valor_hora*self.corte.extra_diurna/100*self.extras*10**2)/10.0**2
        # end if
        return 0
    # end def

    def calcular_hora_nocturna(self):
        valor_hora = self.valor_hora()
        if self.nocturna != None:
            return int(valor_hora*self.corte.nocturna/100*self.nocturna*10**2)/10.0**2
        # end if
        return 0
    # end def

    def calcular_hora_extra_nocturna(self):
        valor_hora = self.valor_hora()
        if self.extra_nocturna != None:
            return int(valor_hora*self.corte.extra_nocturna/100*self.extra_nocturna*10**2)/10.0**2
        # end if
        return 0
    # end def

    def calcular_hora_dominical_diurna(self):
        valor_hora = self.valor_hora()
        if self.dominical_diurna != None:
            return int(valor_hora*self.corte.dominical/100*self.dominical_diurna*10**2)/10.0**2
        # end if
        return 0
    # end def

    def calcular_hora_dominical_nocturna(self):
        valor_hora = self.valor_hora()
        if self.dominical_nocturna != None:
            return int(valor_hora*self.corte.nocturna_dominical/100*self.dominical_nocturna*10**2)/10.0**2
        # end if
        return 0
    # end def

    def calcular_hora_dominical_extra_diurna(self):
        valor_hora = self.valor_hora()
        if self.extra_dominical_diurna != None:
            return int(valor_hora*self.corte.extra_dominical_diurna/100*self.extra_dominical_diurna*10**2)/10.0**2
        # end if
        return 0
    # end def

    def calcular_hora_dominical_extra_nocturna(self):
        valor_hora = self.valor_hora()
        if self.extra_dominical_nocturna != None:
            return int(valor_hora*self.corte.extra_dominical_nocturna/100*self.extra_dominical_nocturna*10**2)/10.0**2
        # end if
        return 0
    # end def

    class Meta:
        unique_together = ('empleado', 'corte')
    # end class

    def __unicode__(self):
        return u"Nomina %s %s - %s" % (self.empleado.nombre, self.empleado.apellidos, self.fecha.strftime('%Y-%m-%d'))
    # end def

# end class
