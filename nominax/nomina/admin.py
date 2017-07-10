# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms

class NominaAdmin(admin.ModelAdmin):
	form = forms.NominaForm
	list_display = ['empleado', 'diurnas','calcular_hora_extra_diurna', 'calcular_hora_nocturna', 'calcular_hora_extra_nocturna', 'calcular_hora_dominical_diurna', 'calcular_hora_dominical_nocturna', 'calcular_hora_dominical_extra_diurna', 'calcular_hora_dominical_extra_nocturna']
	readonly_fields = ['valor_hora', 'recargos', 'salario_legal', 'adelanto', 'prestaciones_sociales', 'descuento_salud', 'bonificacion', 'neto', 'total']
	list_filter = ['id', 'empleado', 'corte']
# end class

class CorteAdmin(admin.ModelAdmin):
	readonly_fields = ['fecha_inicio', 'fecha_fin']
admin.site.register(models.Corte, CorteAdmin)
admin.site.register(models.Nomina, NominaAdmin)

