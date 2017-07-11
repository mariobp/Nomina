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
	#recargos = fields.Field()
	#neto = fields.Field()
	
	#salario_legal = fields.Field()

	identificacion_tipo = fields.Field(column_name="Tipo de Identificacion")
	identificacion = fields.Field(column_name="Numero de Identificacion", attribute="contrato__empleado__cedula")
	nombre = fields.Field(column_name="Nombre", attribute="contrato__empleado__nombre")
	apellidos = fields.Field(column_name="Apellido", attribute="contrato__empleado__apellidos")
	banco_codigo = fields.Field(column_name="Codigo del Banco", attribute="contrato__empleado__cuenta__banco__codigo")
	tipo_producto = fields.Field(column_name="Tipo de Producto o servicio")
	numero = fields.Field(column_name="Numero del producto o servicio", attribute="contrato__empleado__cuenta__numero")
	total = fields.Field(column_name="Valor de Pago o de la recarga")

	def dehydrate_identificacion_tipo(self, nomina):
		return '2'
	#end def

	def dehydrate_tipo_producto(self, nomina):
		return 'CA'
	#end def	

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
		fields = ['identificacion_tipo', 'identificacion', 'nombre', 'apellidos', 'banco_codigo', 'tipo_producto', 'numero', 'total']
		export_order = ['identificacion_tipo', 'identificacion', 'nombre', 'apellidos', 'banco_codigo', 'tipo_producto', 'numero', 'total']
	# end class
#end class

class NominaFResource(resources.ModelResource):
	#ventas = fields.Field(column_name="Ventas", attribute="ventas")
	recargos = fields.Field()
	neto = fields.Field()
	salario_legal = fields.Field()

	total = fields.Field(column_name="Valor de Pago o de la recarga")

	def dehydrate_identificacion_tipo(self, nomina):
		return '2'
	#end def

	def dehydrate_tipo_producto(self, nomina):
		return 'CA'
	#end def	

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
		fields = ['contrato__empleado__pension__nombre','contrato__empleado__eps__nombre','contrato__empleado__nombre', 'contrato__empleado__apellidos', 'corte__fecha_fin', 'contrato__empleado__cargo__nombre', 'salario_base', 'contrato__subsidio_transporte', 'extras', 'dominical_diurna', 'extra_dominical_diurna', 'nocturna', 'extra_nocturna', 'dominical_nocturna', 'extra_dominical_nocturna', 'recargos', 'salario_legal', 'contrato__empleado__cuenta__banco__nombre', 'contrato__empleado__cuenta__numero', 'total']
		export_order = ['contrato__empleado__nombre', 'contrato__empleado__apellidos', 'contrato__empleado__pension__nombre','contrato__empleado__eps__nombre', 'corte__fecha_fin', 'contrato__empleado__cargo__nombre', 'salario_base', 'contrato__subsidio_transporte', 'extras', 'dominical_diurna', 'extra_dominical_diurna', 'nocturna', 'extra_nocturna', 'dominical_nocturna', 'extra_dominical_nocturna', 'recargos', 'salario_legal', 'contrato__empleado__cuenta__banco__nombre', 'contrato__empleado__cuenta__numero', 'total']
	# end class
#end class



reports.register_export(Nomina, NominaResource)
