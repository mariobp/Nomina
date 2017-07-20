# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms
from django.contrib.humanize.templatetags.humanize import intcomma

class NominaAdmin(admin.ModelAdmin):
	form = forms.NominaForm
	list_display = ['contrato', 'diurnas', 'nocturna', 'dominical_diurna', 'dominical_nocturna', 'extras', 'extra_nocturna', 'extra_dominical_diurna', 'extra_dominical_nocturna']
	list_filter = ['id', 'contrato__empleado', 'corte']
	readonly_fields = [
		'salario_base',
		'subsidio_transporte',
		'calcular_hora_diurna',
		'calcular_hora_extra_diurna',
		'calcular_hora_nocturna',
		'calcular_hora_extra_nocturna',
		'calcular_hora_dominical_diurna',
		'calcular_hora_dominical_nocturna',
		'calcular_hora_dominical_extra_diurna',
		'calcular_hora_dominical_extra_nocturna',
		'recargos',
		'total_devengado',
		'descuento_salud',
		'descuentos_adicionales',
		'total_deducido',
		'total',
		'adelanto',
		'bonificacion_neta',
		'descuento_bonificacion',
		'bonificacion',
		'neto',
		'total_pagar',
		'descuento_produccion',
	]

	def salario_base(self, obj):
		return intcomma(round(obj.salario_base, 2))
	# end def

	def subsidio_transporte(self, obj):
		return intcomma(round(obj.subsidio_transporte, 2))
	# end def

	def recargos(self, obj):
		return intcomma(round(obj.recargos, 2))
	# end def

	def total_devengado(self, obj):
		return intcomma(round(obj.total_devengado, 2))
	# end def

	def calcular_hora_diurna(self, obj):
		return intcomma(round(obj.calcular_hora_diurna, 2))
	# end def

	def calcular_hora_extra_diurna(self, obj):
		return intcomma(round(obj.calcular_hora_extra_diurna, 2))
	# end def

	def calcular_hora_nocturna(self, obj):
		return intcomma(round(obj.calcular_hora_nocturna, 2))
	# end def

	def calcular_hora_extra_nocturna(self, obj):
		return intcomma(round(obj.calcular_hora_extra_nocturna, 2))
	# end def

	def calcular_hora_dominical_diurna(self, obj):
		return intcomma(round(obj.calcular_hora_dominical_diurna, 2))
	# end def

	def calcular_hora_dominical_nocturna(self, obj):
		return intcomma(round(obj.calcular_hora_dominical_nocturna, 2))
	# end def

	def calcular_hora_dominical_extra_diurna(self, obj):
		return intcomma(round(obj.calcular_hora_dominical_extra_diurna, 2))
	# end def

	def calcular_hora_dominical_extra_nocturna(self, obj):
		return intcomma(round(obj.calcular_hora_dominical_extra_nocturna, 2))
	# end def

	def descuento_salud(self, obj):
		return intcomma(round(obj.descuento_salud, 2))
	# end def

	def descuentos_adicionales(self, obj):
		return intcomma(round(obj.descuento, 2))
	# end def

	def total_deducido(self, obj):
		return intcomma(round(obj.total_deducido, 2))
	# end def

	def total(self, obj):
		return intcomma(round(obj.total, 2))
	# end def

	def adelanto(self, obj):
		return intcomma(round(obj.adelanto, 2))
	# end def

	def bonificacion_neta(self, obj):
		return intcomma(round(obj.bonificacion_neta, 2))
	# end def

	def descuento_bonificacion(self, obj):
		return intcomma(round(obj.descuento_bonificacion, 2))
	# end def

	def bonificacion(self, obj):
		return intcomma(round(obj.bonificacion, 2))
	# end def

	def neto(self, obj):
		return intcomma(round(obj.neto, 2))
	# end def

	def total_pagar(self, obj):
		return intcomma(round(obj.total_pagar, 2))
	# end def

# end class

class CorteAdmin(admin.ModelAdmin):
	readonly_fields = []

class DescuentoAdmin(admin.ModelAdmin):
	form = forms.DescuentoForm

admin.site.register(models.Corte, CorteAdmin)
admin.site.register(models.Nomina, NominaAdmin)
admin.site.register(models.Descuento, DescuentoAdmin)

