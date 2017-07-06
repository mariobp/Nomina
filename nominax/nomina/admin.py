# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms

class NominaAdmin(admin.ModelAdmin):
	form = forms.NominaForm
	list_display = ['empleado', 'diurnas','calcular_hora_extra_diurna', 'calcular_hora_nocturna', 'calcular_hora_extra_nocturna', 'calcular_hora_dominical_diurna', 'calcular_hora_dominical_nocturna', 'calcular_hora_dominical_extra_diurna', 'calcular_hora_dominical_extra_nocturna']
	readonly_fields = ['valor_hora', 'recargos', 'salario_legal', 'salario_produccion', 'prestaciones_sociales', 'descuento_salud', 'bonificacion', 'neto', 'total']
	list_filter = ['id']
# end class

admin.site.register(models.Corte)
admin.site.register(models.Nomina, NominaAdmin)

