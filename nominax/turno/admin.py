# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms

class DiaDominicalAdmin(admin.ModelAdmin):
	list_display = ['dia', 'proximo', 'anterior']

class TurnoAdmin(admin.ModelAdmin):
	list_display = ['empleado', 'entrada', 'salida', 'horas_extras', 'horas_nocturna', 'horas_diurna', 'horas_dominical', 'total_horas', 'get_extras_diurnas']
	readonly_fields = ['extras', 'nocturna', 'diurna', 'dominical']
	list_filter = ['empleado']

	form = forms.TurnoForm
admin.site.register(models.Turno, TurnoAdmin)
admin.site.register(models.DiaFestivo)
admin.site.register(models.DiaDominical, DiaDominicalAdmin)
