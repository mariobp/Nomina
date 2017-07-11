# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from recursos_h import models as recursos
from datetime import date, timedelta
from turno.datedelta import datedelta, multi_datedelta
from turno import models as turno
from django.db.models import Q, Sum, Count, F, ExpressionWrapper
from decimal import Decimal, getcontext


class Corte(models.Model):
    fecha_inicio = models.DateField()
    fecha_de_adelanto = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    cerrado = models.BooleanField(default=False)

    nocturna = models.IntegerField("Valor de recargo nocturno %")
    dominical = models.IntegerField("Valor de recargo dominical o festivo %")
    nocturna_dominical = models.IntegerField("Valor de recargo nocturno dominical o festivo %")
    descuento_salud = models.IntegerField("Descuento de salud y pensión para empleado %")
    prestaciones_sociales = models.IntegerField("Pago de salud y pensión del empleador %")
    tarifario = models.ManyToManyField(recursos.Tarifario)

    extra_diurna = models.IntegerField("Valor de recargo de hora extra diurna %")
    extra_nocturna = models.IntegerField("Valor de recargo de hora extra nocturna %")

    extra_dominical_diurna = models.IntegerField("Valor de recargo de hora extra dominical %")
    extra_dominical_nocturna = models.IntegerField("Valor de recargo de hora extra dominical nocturna %")

    def __unicode__(self):
        return "%s-%s" % (str(self.fecha_inicio), str(self.fecha_fin))

    @staticmethod
    def get_instance():
        return Corte.objects.filter(cerrado=False).order_by('fecha_inicio').last()
    # end def
# end class

class Nomina(models.Model):
    inicio_mes = models.DateField(blank=True, null=True)

    empleado = models.ForeignKey(recursos.Empleado)
    contrato = models.ForeignKey(recursos.Contrato, blank=True)
    corte = models.ForeignKey(Corte)
    fecha = models.DateField(auto_now_add=True)

    diurnas = models.DecimalField("Hora diurna", blank=True, null=True, max_digits=10, decimal_places=2, )
    nocturna = models.DecimalField("Hora nocturna", blank=True, null=True, max_digits=10, decimal_places=2, )
    dominical_diurna = models.DecimalField("Hora dominical diurna", blank=True, null=True, max_digits=10, decimal_places=2, )
    dominical_nocturna = models.DecimalField("Hora dominical nocturna", blank=True, null=True, max_digits=10, decimal_places=2, )
    
    extras = models.DecimalField("Hora extra diurna", blank=True, null=True, max_digits=10, decimal_places=2, )
    extra_nocturna = models.DecimalField("Hora extra nocturna", blank=True, null=True, max_digits=10, decimal_places=2, )
    extra_dominical_diurna = models.DecimalField("Hora extra dominical diurna", blank=True, null=True, max_digits=10, decimal_places=2, )
    extra_dominical_nocturna = models.DecimalField("Hora extra dominical nocturna", blank=True, null=True, max_digits=10, decimal_places=2, )

    def salario_produccion(self, fecha_inicio, fecha_fin):
        tarifas = self.corte.tarifario.values_list('id', flat=True)
        produccion = turno.Produccion.objects.filter(fecha__gte=fecha_inicio, empleados=self.empleado, unidad__tarifario__in=tarifas)
        if fecha_fin:
            produccion = produccion.filter(fecha__lt=fecha_fin)
        # end if
        produccion = produccion.annotate(total=ExpressionWrapper(
                Sum('cantidad')/Count('empleados')*F('unidad__tarifario__precio'), 
                output_field=models.DateTimeField()
            )
        )
        total = 0
        for pro in produccion:
            total = total + pro.total
        # end if
        return total
    # end def

    def salario_produccion_adelanto(self, ):
        return self.salario_produccion(self.corte.fecha_inicio, self.corte.fecha_de_adelanto)
    # end def

    def salario_produccion_nomina(self, ):
        return self.salario_produccion(self.corte.fecha_inicio, self.corte.fecha_fin)
    # end def

    def prestaciones_sociales(self):
        return self.salario_legal()*self.corte.prestaciones_sociales/100
    # end def

    def descuento_salud(self):
        try:
            return (self.salario_legal() - self.contrato.subsidio_transporte)*self.corte.descuento_salud/100
        except Exception as e:
            print e
        return 0
    # end def

    def bonificacion(self):
        bonificacion = self.salario_produccion_adelanto() + self.salario_produccion_nomina() - self.salario_legal()
        if bonificacion < 0:
            return 0
        # end if
        return bonificacion
    # end def

    def valor_hora(self):
        if self.contrato.salario_base:
            return Decimal(self.contrato.salario_base)/Decimal(240)
        # end def
        return 0
    # end def

    def salario_legal(self):
        return (self.contrato.salario_base) + (self.contrato.subsidio_transporte ) + Decimal(self.recargos())
    # end def

    def adelanto(self):
        if self.contrato.tipo_contrato.modalidad == recursos.TipoContrato.PRODUCCION:
            return self.salario_produccion_adelanto()
        # end if
        return 0
    # end def

    def neto(self):
        if self.contrato.tipo_contrato.modalidad == recursos.TipoContrato.SALARIO_FIJO:
            return self.salario_legal()
        elif self.contrato.tipo_contrato.modalidad == recursos.TipoContrato.PRODUCCION:
            if self.salario_produccion_adelanto() + self.salario_produccion_nomina() < (self.contrato.salario_base or 0):
                return self.salario_legal() - self.salario_produccion_adelanto()
            # end if
            return self.salario_produccion_nomina()
        # end if
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
