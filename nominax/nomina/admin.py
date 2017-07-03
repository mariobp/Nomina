# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms

class NominaAdmin(admin.ModelAdmin):
	form = forms.NominaForm
	list_display = ['calcular_hora_extra_diurna', 'calcular_hora_nocturna', 'calcular_hora_extra_nocturna', 'calcular_hora_dominical_diurna', 'calcular_hora_dominical_nocturna', 'calcular_hora_dominical_extra_diurna', 'calcular_hora_dominical_extra_nocturna']

# end class

admin.site.register(models.Corte)
admin.site.register(models.Nomina, NominaAdmin)

