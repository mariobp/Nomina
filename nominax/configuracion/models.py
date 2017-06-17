# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from cuser.fields import CurrentUserField
# Create your models here.


class Configuracion(models.Model):
    opciones = (
        (0, "Quincenal"),
        (1, "Mensual")
    )
    tipo_corte = models.IntegerField(choices=opciones)
    primer_dia = models.PositiveIntegerField("Primer dia de corte", validators=[MaxValueValidator(31)])
    segundo_dia = models.PositiveIntegerField("Segundo dia de corte", validators=[MaxValueValidator(31)], blank=True, null=True)
    h_recargo_nocturno = models.TimeField()
    creator = CurrentUserField(add_only=True, related_name="created_configuracion")
    last_editor = CurrentUserField(related_name="last_edited_configuracion")

    class Meta:
        verbose_name = "Configucarión"
        verbose_name_plural = "Configuraciones"
    # end class

    def __unicode__(self):
        if tipo_corte == 1:
            tipo = "Quincenal"
        else:
            tipo = "Mensual"
        # end if
        if segundo_dia:
            segundo = str(self.segundo_dia)
        else:
            segundo = "Ninguno"
        # end if
        return u"Configuración %s Primer Dia %d Segundo dia %s" % (tipo, self.primer_dia, segundo)
    # end def
# end class


"""
class Concepto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField()
"""
