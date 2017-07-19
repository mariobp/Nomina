# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms

class DiaDominicalAdmin(admin.ModelAdmin):
	list_display = ['dia', 'proximo', 'anterior']

class TurnoAdmin(admin.ModelAdmin):
	list_display = ['empleado', 'aprobado', 'descontar_almuerzo', 'entrada', 'salida', 'horas_extras', 'horas_nocturna', 'horas_diurna', 'horas_dominical', 'total_horas']
	readonly_fields = ['extras', 'nocturna', 'diurna', 'dominical']
	list_filter = ['empleado', 'aprobado']

	def get_queryset(self, *args, **kwargs):
		queryset = super(TurnoAdmin, self).get_queryset(*args, **kwargs)
		queryset = queryset.filter(empleado__pk=15)
		#queryset.update(aprobado=True)
		diurnas = 0
		nocturnas = 0
		total = 0
		for turno in queryset:
			horas_diurna = turno.horas_diurna()
			horas_nocturna = turno.horas_nocturna()
			total_horas = turno.total_horas()

			diurnas = diurnas + horas_diurna
			nocturnas = nocturnas + horas_nocturna
			total = total + total_horas
			
		# 	forms.TurnoForm.update_form(turno, {})
		print diurnas, nocturnas, total
		return queryset
	# end def

	form = forms.TurnoForm
# end class

class ProduccionAdmin(admin.ModelAdmin):
	list_display=['fecha', 'unidad', 'cantidad', ]
admin.site.register(models.Turno, TurnoAdmin)
admin.site.register(models.DiaFestivo)
admin.site.register(models.Produccion, ProduccionAdmin)
admin.site.register(models.DiaDominical, DiaDominicalAdmin)
