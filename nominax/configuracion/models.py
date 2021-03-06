# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from cuser.fields import CurrentUserField
from recursos_h import models as recursos

class Configuracion(models.Model):
    opciones = (
        (0, "Quincenal"),
        (1, "Mensual")
    )

    tipo_cuenta_choices = (
        ('S', "Ahorros"),
        ('D', 'Corriente')
    )

    tipo_corte = models.IntegerField(choices=opciones)
    primer_dia = models.PositiveIntegerField("Primer dia de corte", validators=[MaxValueValidator(31)])
    segundo_dia = models.PositiveIntegerField("Segundo dia de corte", validators=[MaxValueValidator(31)], blank=True, null=True)
    
    nit = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=100)
    tipo_cuenta = models.CharField(max_length=2, choices=tipo_cuenta_choices)

    h_recargo_nocturno_inicio = models.TimeField("Hora de inicio de recargo nocturno")
    h_recargo_nocturno_fin = models.TimeField("Hora de finalización de recargo nocturno")
    h_almuerzo_inicio = models.TimeField("Hora de inicio de almuerzo")
    h_almuerzo_fin = models.TimeField("Hora de fin de almuerzo")

    tarifario = models.ManyToManyField(recursos.Tarifario)

    salario_minimo_dia = models.IntegerField("salario minimo legal vigente diario")
    descuento_salud = models.IntegerField("Descuento de salud y pensión para empleado %")

    nocturna = models.IntegerField("Valor de recargo nocturno %")
    dominical = models.IntegerField("Valor de recargo dominical o festivo %")
    nocturna_dominical = models.IntegerField("Valor de recargo nocturno dominical o festivo %")
    
    extra_diurna = models.IntegerField("Valor de recargo de hora extra diurna %")
    extra_nocturna = models.IntegerField("Valor de recargo de hora extra nocturna %")

    extra_dominical_diurna = models.IntegerField("Valor de recargo de hora extra dominical %")
    extra_dominical_nocturna = models.IntegerField("Valor de recargo de hora extra dominical nocturna %")

    creator = CurrentUserField(add_only=True, related_name="created_configuracion")
    last_editor = CurrentUserField(related_name="last_edited_configuracion")

    @staticmethod
    def get_instance():
        return Configuracion.objects.last()
    # end def

    class Meta:
        verbose_name = "Configucarión"
        verbose_name_plural = "Configuraciones"
    # end class

    def __unicode__(self):
        if self.tipo_corte == 1:
            tipo = "Quincenal"
        else:
            tipo = "Mensual"
        # end if
        if self.segundo_dia:
            segundo = str(self.segundo_dia)
        else:
            segundo = "Ninguno"
        # end if
        return u"Configuración %s Primer Dia %d Segundo dia %s" % (tipo, self.primer_dia, segundo)
    # end def
# end class


class Concepto(models.Model):
    opciones = (
        (1, 'Extras'),
        (2, 'Extra nocturna'),
        (3, 'Extra diurna'),
        (4, 'Extra dominical')
    )
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    referencia = models.IntegerField(choices=opciones)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class
