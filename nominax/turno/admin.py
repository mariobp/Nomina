# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

class DiaDominicalAdmin(admin.ModelAdmin):
	list_display = ['dia', 'proximo', 'anterior']

class TurnoAdmin(admin.ModelAdmin):
	list_display = ['empleado', 'entrada', 'salida', 'horas_extras', 'horas_nocturna', 'horas_diurna', 'horas_dominical']
admin.site.register(models.Turno, TurnoAdmin)
admin.site.register(models.DiaFestivo)
admin.site.register(models.DiaDominical, DiaDominicalAdmin)
