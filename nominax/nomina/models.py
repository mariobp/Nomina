# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from recursos_h import models as recursos
from datetime import date, timedelta
from turno.datedelta import datedelta, multi_datedelta
from turno import models as turno
from django.db.models import Q, Sum, Count, F, ExpressionWrapper
from django.contrib.auth.models import User
from decimal import Decimal, getcontext
from django.utils.functional import cached_property


class Corte(models.Model):
    fecha_inicio = models.DateField()
    fecha_de_adelanto = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    cerrado = models.BooleanField(default=False)

    nocturna = models.IntegerField("Valor de recargo nocturno %", blank=True)
    dominical = models.IntegerField("Valor de recargo dominical o festivo %", blank=True)
    nocturna_dominical = models.IntegerField("Valor de recargo nocturno dominical o festivo %", blank=True)
    descuento_salud = models.IntegerField("Descuento de salud y pensión para empleado %", blank=True)
    tarifario = models.ManyToManyField(recursos.Tarifario, blank=True)

    extra_diurna = models.IntegerField("Valor de recargo de hora extra diurna %", blank=True)
    extra_nocturna = models.IntegerField("Valor de recargo de hora extra nocturna %", blank=True)

    extra_dominical_diurna = models.IntegerField("Valor de recargo de hora extra dominical %", blank=True)
    extra_dominical_nocturna = models.IntegerField("Valor de recargo de hora extra dominical nocturna %", blank=True)

    def __unicode__(self):
        return "%s-%s" % (str(self.fecha_inicio), str(self.fecha_fin))
    # end def

    @staticmethod
    def get_instance():
        return Corte.objects.filter(cerrado=False).order_by('fecha_inicio').last()
    # end def
# end class

class Descuento(models.Model):
    corte = models.ForeignKey(Corte, blank=True)
    concepto = models.CharField(max_length=120)
    contratos = models.ManyToManyField(recursos.Contrato)
    cantidad = models.DecimalField("Cantidad $", max_digits=10, decimal_places=2)
    recurrente = models.BooleanField(default=False)
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_descuento", blank=True, null=True)

    def empleados(self):
        pks = self.contratos.all().values('id')
        empleados = recursos.Empleado.objects.filter(contrato__in=pks)
        string = ""
        for empleado in empleados:
            string = string + empleado.nombre + ' ' + empleado.apellidos + ', '
        # end for
        return string
    # end def

    @staticmethod
    def get_descuento(contrato, corte):
        descuentos = Descuento.objects.filter(contratos=contrato, corte=corte, eliminado=False).annotate(total=Sum('cantidad')).first()
        recurrentes = Descuento.objects.filter(contratos=contrato, corte__fecha_inicio__lt=corte.fecha_inicio, recurrente=True).annotate(total=Sum('cantidad')).first()
        total = 0
        if descuentos:
            return descuentos.total
        # end if
        if recurrentes:
            return recurrentes.total
        # end if
        return total
    # end def
# end class

class DiaIncapacidad(models.Model):
    fecha = models.DateField()
    empleado = models.ForeignKey(recursos.Empleado)
    dias = models.IntegerField()
# end class

class DescuentoProduccion(models.Model):
    fecha  = models.DateTimeField(auto_now_add=True)
    corte = models.ForeignKey(Corte, blank=True)
    unidad = models.ForeignKey(recursos.UnidadProduccion)
    cantidad = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    concepto = models.CharField(max_length=120)
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_descuentop", blank=True, null=True)
# end class

class Nomina(models.Model):
    inicio_mes = models.DateField(blank=True, null=True)

    contrato = models.ForeignKey(recursos.Contrato, blank=True)
    corte = models.ForeignKey(Corte, blank=True)
    fecha = models.DateField(auto_now_add=True)

    diurnas = models.DecimalField("Hora diurna", blank=True, null=True, max_digits=10, decimal_places=2, )
    nocturna = models.DecimalField("Hora nocturna", blank=True, null=True, max_digits=10, decimal_places=2, )
    dominical_diurna = models.DecimalField("Hora dominical diurna", blank=True, null=True, max_digits=10, decimal_places=2, )
    dominical_nocturna = models.DecimalField("Hora dominical nocturna", blank=True, null=True, max_digits=10, decimal_places=2, )
    
    extras = models.DecimalField("Hora extra diurna", blank=True, null=True, max_digits=10, decimal_places=2, )
    extra_nocturna = models.DecimalField("Hora extra nocturna", blank=True, null=True, max_digits=10, decimal_places=2, )
    extra_dominical_diurna = models.DecimalField("Hora extra dominical diurna", blank=True, null=True, max_digits=10, decimal_places=2, )
    extra_dominical_nocturna = models.DecimalField("Hora extra dominical nocturna", blank=True, null=True, max_digits=10, decimal_places=2, )

    def get_produccion(self, fecha_inicio, fecha_fin):
        tarifas = self.corte.tarifario.values_list('id', flat=True)
        produccion = turno.Produccion.objects.filter(fecha__gte=fecha_inicio, empleados=self.contrato.empleado, unidad__tarifario__in=tarifas).distinct('id')
        if fecha_fin:
            produccion = produccion.filter(fecha__lt=fecha_fin)
        # end if
        return produccion
    # end def

    def salario_produccion(self, fecha_inicio, fecha_fin):
        produccion = self.get_produccion(fecha_inicio, fecha_fin)
        total = 0
        for pro in produccion:
            tarifa = recursos.Tarifario.objects.filter(unidad=pro.unidad, cargo=self.contrato.empleado.cargo, remplazado_por__isnull=True).last()
            sub_total = pro.cantidad/pro.empleados.count()*tarifa.precio 
            total = total + sub_total
        # end for
        return total
    # end def

    @cached_property
    def descuento_produccion(self):
        try:
            descuentos = DescuentoProduccion.objects.filter(corte=self.corte, eliminado=False)
            produccion = self.get_produccion(self.corte.fecha_inicio, self.corte.fecha_fin)
            total = 0
            for des in descuentos:
                pros = produccion.filter(unidad=des.unidad).count()
                total = total + des.cantidad/pros
            # end for
            return total
        except Exception as e:
            print e
        # end try
    # end def

    @cached_property
    def salario_base(self):
        return self.contrato.salario_base
    # end def

    @cached_property
    def subsidio_transporte(self):
        return self.contrato.subsidio_transporte
    # end def

    @cached_property
    def total_devengado(self):
        return self.salario_base + self.subsidio_transporte + Decimal(self.recargos)
    # end def

    @cached_property
    def salario_produccion_total(self):
        return self.salario_produccion_adelanto + self.salario_produccion_nomina
    # end def

    @cached_property
    def salario_produccion_adelanto(self):
        adelanto = self.salario_produccion(self.corte.fecha_inicio, self.corte.fecha_de_adelanto)
        if self.descuento_produccion > adelanto:
            return 0
        # end if
        return adelanto
    # end def

    @cached_property
    def salario_produccion_nomina(self):
        nomina = self.salario_produccion(self.corte.fecha_de_adelanto, self.corte.fecha_fin)
        adelanto = self.salario_produccion(self.corte.fecha_inicio, self.corte.fecha_de_adelanto)
        if self.descuento_produccion > adelanto:
            return nomina - (self.descuento_produccion - adelanto)
        # end if
        return nomina
    # end def

    @cached_property
    def descuento_salud(self):
        try:
            return (self.total_devengado - self.contrato.subsidio_transporte)*self.corte.descuento_salud/100
        except Exception as e:
            print e
        return 0
    # end def

    @cached_property
    def bonificacion(self):
        return self.bonificacion_neta - self.descuento_bonificacion
    # end def

    @cached_property
    def descuento_bonificacion(self):
        percent = self.total_devengado*Decimal(0.4)
        if self.bonificacion_neta > percent:
            return self.bonificacion_neta - percent
        # end if
        return 0
    # end def

    @cached_property
    def bonificacion_neta(self):
        bonificacion = self.salario_produccion_adelanto + self.salario_produccion_nomina - self.total_devengado
        if bonificacion < 0:
            return 0
        # end if
        return bonificacion        
    # end def

    @cached_property
    def valor_hora(self):
        if self.contrato.salario_base:
            return Decimal(self.contrato.salario_base)/Decimal(240)
        # end def
        return 0
    # end def

    @cached_property
    def adelanto(self):
        if self.contrato.tipo_contrato.modalidad == recursos.TipoContrato.PRODUCCION:
            return self.salario_produccion_adelanto
        elif self.contrato.tipo_contrato.modalidad == recursos.TipoContrato.SALARIO_FIJO:
            return self.salario_base/2
        # end if
        return 0
    # end def

    @cached_property
    def neto(self):
        if self.contrato.tipo_contrato.modalidad == recursos.TipoContrato.SALARIO_FIJO:
            return self.total
        elif self.contrato.tipo_contrato.modalidad == recursos.TipoContrato.PRODUCCION:
            if self.salario_produccion_adelanto + self.salario_produccion_nomina < self.total_devengado:
                return self.total_devengado - self.salario_produccion_adelanto
            # end if
            return self.bonificacion + self.total_devengado
        # end if
        return 0
    # end def

    @cached_property
    def descuento(self):
        try:
            return Descuento.get_descuento(self.contrato, self.corte)
        except Exception as a:
            print a
        # end try
    # end def

    @cached_property
    def total_deducido(self):
        return self.descuento_salud + self.descuento
    # end def

    @cached_property
    def total(self):
        return self.total_devengado - self.total_deducido
    # end def

    @cached_property
    def total_pagar(self):
        return self.neto - self.adelanto
    # end def

    @cached_property
    def recargos(self):
        recargos = 0
        recargos = recargos + self.calcular_hora_extra_diurna
        recargos = recargos + self.calcular_hora_nocturna
        recargos = recargos + self.calcular_hora_extra_nocturna
        recargos = recargos + self.calcular_hora_dominical_diurna
        recargos = recargos + self.calcular_hora_dominical_nocturna
        recargos = recargos + self.calcular_hora_dominical_extra_diurna
        recargos = recargos + self.calcular_hora_dominical_extra_nocturna
        return recargos
    # end def

    @cached_property
    def calcular_hora_diurna(self):
        valor_hora = self.valor_hora
        if self.diurnas != None:
            return valor_hora*self.diurnas
        # end if
        return 0
    # end def

    @cached_property
    def calcular_hora_extra_diurna(self):
        valor_hora = self.valor_hora
        if self.extras != None:
            return valor_hora*self.corte.extra_diurna/100*self.extras
        # end if
        return 0
    # end def

    @cached_property
    def calcular_hora_nocturna(self):
        valor_hora = self.valor_hora
        if self.nocturna != None:
            return valor_hora*self.corte.nocturna/100*self.nocturna
        # end if
        return 0
    # end def

    @cached_property
    def calcular_hora_extra_nocturna(self):
        valor_hora = self.valor_hora
        if self.extra_nocturna != None:
            return valor_hora*self.corte.extra_nocturna/100*self.extra_nocturna
        # end if
        return 0
    # end def

    @cached_property
    def calcular_hora_dominical_diurna(self):
        valor_hora = self.valor_hora
        if self.dominical_diurna != None:
            return valor_hora*self.corte.dominical/100*self.dominical_diurna
        # end if
        return 0
    # end def

    @cached_property
    def calcular_hora_dominical_nocturna(self):
        valor_hora = self.valor_hora
        if self.dominical_nocturna != None:
            return valor_hora*self.corte.nocturna_dominical/100*self.dominical_nocturna
        # end if
        return 0
    # end def

    @cached_property
    def calcular_hora_dominical_extra_diurna(self):
        valor_hora = self.valor_hora
        if self.extra_dominical_diurna != None:
            return valor_hora*self.corte.extra_dominical_diurna/100*self.extra_dominical_diurna
        # end if
        return 0
    # end def

    @cached_property
    def calcular_hora_dominical_extra_nocturna(self):
        valor_hora = self.valor_hora
        if self.extra_dominical_nocturna != None:
            return valor_hora*self.corte.extra_dominical_nocturna/100*self.extra_dominical_nocturna
        # end if
        return 0
    # end def

    def __unicode__(self):
        return u"Nomina %s %s - %s" % (self.contrato.empleado.nombre, self.contrato.empleado.apellidos, self.fecha.strftime('%Y-%m-%d'))
    # end def

# end class
