# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms

class NominaAdmin(admin.ModelAdmin):
	form = forms.NominaForm
	list_display = ['contrato', 'diurnas', 'nocturna', 'dominical_diurna', 'dominical_nocturna', 'extras', 'extra_nocturna', 'extra_dominical_diurna', 'extra_dominical_nocturna']
	readonly_fields = ['descuento', 'valor_hora', 'recargos', 'salario_legal', 'adelanto', 'descuento_salud', 'bonificacion', 'neto', 'total']
	list_filter = ['id', 'contrato__empleado', 'corte']
# end class

class CorteAdmin(admin.ModelAdmin):
	readonly_fields = []

class DescuentoAdmin(admin.ModelAdmin):
	form = forms.DescuentoForm

admin.site.register(models.Corte, CorteAdmin)
admin.site.register(models.Nomina, NominaAdmin)
admin.site.register(models.Descuento, DescuentoAdmin)

