#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @author: Exile
    @date: 05-07-2016
    @place: Cartagena - Colombia
    @licence: Creative Common
"""
import reports
from import_export import resources, widgets, fields
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from nomina.models import Nomina
from django.db.models import Count

class NominaResource(resources.ModelResource):
	#ventas = fields.Field(column_name="Ventas", attribute="ventas")
	recargos = fields.Field()
	neto = fields.Field()
	total = fields.Field()
	salario_legal = fields.Field()

	def dehydrate_salario_legal(self, nomina):
		return nomina.salario_legal()
	#end def

	def dehydrate_recargos(self, nomina):
		return nomina.recargos()
	#end def

	def dehydrate_neto(self, nomina):
		return nomina.neto()
	#end def

	def dehydrate_total(self, nomina):
		return nomina.total()
	#end def

	class Meta:
		model = Nomina
		fields = ['empleado__pension__nombre','empleado__eps__nombre','empleado__nombre', 'empleado__apellidos', 'corte__fecha_fin', 'empleado__cargo__nombre', 'salario_base', 'subsidio_trasporte', 'extras', 'dominical_diurna', 'extra_dominical_diurna', 'nocturna', 'extra_nocturna', 'dominical_nocturna', 'extra_dominical_nocturna', 'recargos', 'salario_legal']
	# end class
#end class
reports.register_export(Nomina, NominaResource)
