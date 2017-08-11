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
from turno.models import Turno
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
	banco_codigo = fields.Field(column_name="Codigo del Banco", attribute="contrato__empleado__banco__codigo")
	tipo_producto = fields.Field(column_name="Tipo de Producto o servicio")
	numero = fields.Field(column_name="Numero del producto o servicio", attribute="contrato__empleado__numero")
	total = fields.Field(column_name="Valor de Pago o de la recarga")

	def dehydrate_identificacion_tipo(self, nomina):
		return '2'
	#end def

	def dehydrate_tipo_producto(self, nomina):
		return 'CA'
	#end def	

	def dehydrate_salario_legal(self, nomina):
		return nomina.total_devengado
	#end def

	def dehydrate_recargos(self, nomina):
		return nomina.recargos
	#end def

	def dehydrate_neto(self, nomina):
		return nomina.neto
	#end def

	def dehydrate_total(self, nomina):
		return nomina.total
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
	bonificacion = fields.Field()
	descuento_salud = fields.Field()
	descuento_salud_half = fields.Field()

	total = fields.Field(column_name="Valor de Pago o de la recarga")

	def dehydrate_identificacion_tipo(self, nomina):
		return '2'
	#end def

	def dehydrate_tipo_producto(self, nomina):
		return 'CA'
	#end def	

	def dehydrate_salario_legal(self, nomina):
		return float(nomina.total_devengado)
	#end def

	def dehydrate_recargos(self, nomina):
		return nomina.recargos
	#end def

	def dehydrate_neto(self, nomina):
		return float(nomina.neto)
	#end def

	def dehydrate_total(self, nomina):
		return "%.2f" % float(nomina.total)
	#end def

	def dehydrate_bonificacion(self, nomina):
		return nomina.bonificacion
	#end def

	def dehydrate_descuento_salud(self, nomina):
		return "%.2f" % float(nomina.descuento_salud)
	#end def

	def dehydrate_descuento_salud_half(self, nomina):
		return "%.2f" % float(nomina.descuento_salud/2)
	#end def

	class Meta:
		model = Nomina
		fields = ['contrato__empleado__nombre', 'contrato__empleado__apellidos', 'corte__fecha_fin', 'contrato__empleado__banco__nombre', 'contrato__empleado__numero', 'contrato__empleado__cargo__nombre', 'contrato__salario_base', 'contrato__subsidio_transporte', 'extras', 'dominical_diurna', 'extra_dominical_diurna', 'nocturna', 'extra_nocturna', 'dominical_nocturna', 'extra_dominical_nocturna', 'salario_legal', 'contrato__empleado__pension__nombre', 'contrato__empleado__eps__nombre', 'recargos', 'neto', 'bonificacion','descuento_salud_half','descuento_salud', 'total']
		export_order = ['contrato__empleado__nombre','contrato__empleado__apellidos', 'corte__fecha_fin', 'contrato__empleado__banco__nombre', 'contrato__empleado__numero', 'contrato__empleado__cargo__nombre', 'contrato__salario_base', 'contrato__subsidio_transporte', 'extras', 'dominical_diurna', 'extra_dominical_diurna', 'nocturna', 'extra_nocturna', 'dominical_nocturna', 'extra_dominical_nocturna', 'salario_legal', 'contrato__empleado__pension__nombre', 'contrato__empleado__eps__nombre', 'recargos', 'neto', 'bonificacion', 'descuento_salud_half','descuento_salud', 'total']
	# end class
#end class

class NominaDescResource(resources.ModelResource):

	descuento_bonificacion = fields.Field(column_name="Descuento en bonificacion")
	empleado = fields.Field(column_name="Empleado")
	cedula = fields.Field(column_name="Cedula", attribute="contrato__empleado__cedula")
	cargo = fields.Field(column_name="Cargo", attribute="contrato__empleado__cargo__nombre")
	corte = fields.Field(column_name="Corte", attribute="corte__fecha_fin")
	cuenta = fields.Field(column_name="Cuenta", attribute="contrato__empleado__numero")
	banco = fields.Field(column_name="Banco", attribute="contrato__empleado__banco__nombre")

	def dehydrate_descuento_bonificacion(self, nomina):
		return "%.2f" % float(nomina.descuento_bonificacion)
	#end def

	def dehydrate_empleado(self, nomina):
		return u'%s %s' % (nomina.contrato.empleado.nombre, nomina.contrato.empleado.apellidos)
	#end def

	class Meta:
		model = Nomina
		fields = ['empleado', 'cedula','cargo', 'corte', 'descuento_bonificacion', 'cuenta', 'banco']
		export_order = ['empleado','cedula','cargo', 'corte', 'descuento_bonificacion', 'cuenta', 'banco']
	# end class
#end class

class NominaResuResource(resources.ModelResource):

	empleado = fields.Field(column_name="Empleado")
	cedula = fields.Field(column_name="Cedula", attribute="contrato__empleado__cedula") 
	cargo = fields.Field(column_name="Cargo", attribute="contrato__empleado__cargo__nombre")
	corte = fields.Field(column_name="Corte", attribute="corte__fecha_fin")
	salario_base = fields.Field(column_name="Salario Base", attribute="contrato__salario_base")
	subsidio_transporte = fields.Field(column_name="Subsidio de Transporte", attribute="contrato__subsidio_transporte")
	recargos = fields.Field(column_name="Recargos", attribute="recargos")
	hora_extra_diurna = fields.Field(column_name="Horas extras diurna")
	hora_nocturna = fields.Field(column_name="Horas nocturnas")
	hora_nocturna_extra = fields.Field(column_name="Horas nocturnas extras")
	dominicales = fields.Field(column_name="Horas dominicales diurnas")
	dominicales_extras = fields.Field(column_name="Horas dominicales diurnas extras")
	dominincales_nocturnas =fields.Field(column_name="Horas dominicales nocturnas")
	dominincales_nocturnas_extras = fields.Field(column_name="Horas dominicales nocturnas extras")
	total_devengado = fields.Field(column_name="Total devengado")
	descuento_salud = fields.Field(column_name="Descuento salud y pension") 
	descuentos_adicionales = fields.Field(column_name="Descuentos adicionales")
	total_deducido = fields.Field(column_name="Total total_deducido") 
	total = fields.Field(column_name="Total")
	adelanto = fields.Field(column_name="Adelanto 1era quincena")
	bonificacion_neta = fields.Field(column_name="Bonificacion neta")
	descuento_bonificacion = fields.Field(column_name="Descuento en bonificacion")
	bonificacion = fields.Field(column_name="Bonificacion")
	neto = fields.Field(column_name="Neto")
	total_pagar = fields.Field(column_name="Total a pagar")


	def dehydrate_recargos(self, nomina):
		return "%.2f" % float(nomina.recargos)
	#end def

	def dehydrate_hora_extra_diurna(self, nomina):
		return "%.2f" % float(nomina.calcular_hora_extra_diurna)
	#end def

	def dehydrate_hora_nocturna(self, nomina):
		return "%.2f" % float(nomina.calcular_hora_nocturna)
	#end def

	def dehydrate_hora_nocturna_extra(self, nomina):
		return "%.2f" % float(nomina.calcular_hora_extra_nocturna)
	#end def

	def dehydrate_dominicales(self, nomina):
		return "%.2f" % float(nomina.calcular_hora_dominical_diurna)
	#end def

	def dehydrate_dominicales_extras(self, nomina):
		return "%.2f" % float(nomina.calcular_hora_dominical_extra_diurna)
	#end def

	def dehydrate_dominincales_nocturnas(self, nomina):
		return "%.2f" % float(nomina.calcular_hora_dominical_nocturna)
	#end def

	def dehydrate_dominincales_nocturnas_extras(self, nomina):
		return "%.2f" % float(nomina.calcular_hora_dominical_extra_nocturna)
	#end def

	def dehydrate_total_devengado(self, nomina):
		return "%.2f" % float(nomina.total_devengado)
	#end def

	def dehydrate_descuento_salud(self, nomina):
		return "%.2f" % float(nomina.descuento_salud)
	#end def

	def dehydrate_descuentos_adicionales(self, nomina):
		return "%.2f" % float(nomina.descuento)
	#end def

	def dehydrate_total_deducido(self, nomina):
		return "%.2f" % float(nomina.total_deducido)
	#end def

	def dehydrate_total(self, nomina):
		return "%.2f" % float(nomina.total)
	#end def

	def dehydrate_adelanto(self, nomina):
		return "%.2f" % float(nomina.adelanto)
	#end def

	def dehydrate_bonificacion_neta(self, nomina):
		return "%.2f" % float(nomina.bonificacion_neta)
	#end def

	def dehydrate_descuento_bonificacion(self, nomina):
		return "%.2f" % float(nomina.descuento_bonificacion)
	#end def

	def dehydrate_bonificacion(self, nomina):
		return "%.2f" % float(nomina.bonificacion)
	#end def

	def dehydrate_neto(self, nomina):
		return "%.2f" % float(nomina.neto)
	#end def

	def dehydrate_total_pagar(self, nomina):
		return "%.2f" % float(nomina.total_pagar)
	#end def

	def dehydrate_empleado(self, nomina):
		return u'%s %s' % (nomina.contrato.empleado.nombre, nomina.contrato.empleado.apellidos)
	#end def

	class Meta:
		model = Nomina
		fields = ['empleado', 'cedula', 'cargo', 'corte', 'salario_base', 'subsidio_transporte', 'recargos', 'hora_extra_diurna', 'hora_nocturna', 'hora_nocturna_extra', 'dominicales', 'dominicales_extras', 'dominincales_nocturnas', 'dominincales_nocturnas_extras', 'total_devengado', 'descuento_salud', 'descuentos_adicionales', 'total_deducido', 'total', 'adelanto', 'bonificacion_neta', 'descuento_bonificacion', 'bonificacion', 'neto', 'total_pagar']
		export_order = ['empleado', 'cedula', 'cargo', 'corte', 'salario_base', 'subsidio_transporte', 'recargos', 'hora_extra_diurna', 'hora_nocturna', 'hora_nocturna_extra', 'dominicales', 'dominicales_extras', 'dominincales_nocturnas', 'dominincales_nocturnas_extras', 'total_devengado', 'descuento_salud', 'descuentos_adicionales', 'total_deducido', 'total', 'adelanto', 'bonificacion_neta', 'descuento_bonificacion', 'bonificacion', 'neto', 'total_pagar']
	# end class
#end class


class TurnoResource(resources.ModelResource):

	empleado = fields.Field(column_name="Empleado")
	cedula = fields.Field(column_name="Cedula", attribute="empleado__cedula") 
	cargo = fields.Field(column_name="Cargo", attribute="empleado__cargo__nombre")
	hora_diurna = fields.Field(column_name="Horas diurnas")
	hora_extra_diurna = fields.Field(column_name="Horas extras diurna")
	hora_nocturna = fields.Field(column_name="Horas nocturnas")
	hora_nocturna_extra = fields.Field(column_name="Horas nocturnas extras")
	dominicales = fields.Field(column_name="Horas dominicales diurnas")
	dominicales_extras = fields.Field(column_name="Horas dominicales diurnas extras")
	dominincales_nocturnas =fields.Field(column_name="Horas dominicales nocturnas")
	dominincales_nocturnas_extras = fields.Field(column_name="Horas dominicales nocturnas extras")

	def dehydrate_hora_diurna(self, turno):
		return "%.2f" % float(turno.show_diurnas())
	#end def

	def dehydrate_hora_extra_diurna(self, turno):
		return "%.2f" % float(turno.show_extra_duirna())
	#end def

	def dehydrate_hora_nocturna(self, turno):
		return "%.2f" % float(turno.show_nocturnas())
	#end def

	def dehydrate_hora_nocturna_extra(self, turno):
		return "%.2f" % float(turno.show_extra_nocturnas())
	#end def

	def dehydrate_dominicales(self, turno):
		return "%.2f" % float(turno.show_dominicales_diurnas())
	#end def

	def dehydrate_dominicales_extras(self, turno):
		return "%.2f" % float(turno.show_dominicales_diurnas_extra())
	#end def

	def dehydrate_dominincales_nocturnas(self, turno):
		return "%.2f" % float(turno.show_dominicales_nocturnas())
	#end def

	def dehydrate_dominincales_nocturnas_extras(self, turno):
		return "%.2f" % float(turno.show_dominicales_nocturnas_extra())
	#end def

	def dehydrate_empleado(self, turno):
		return u'%s %s' % (turno.empleado.nombre, turno.empleado.apellidos)
	#end def

	class Meta:
		model = Nomina
		fields = ['empleado', 'cedula', 'cargo', 'hora_diurna', 'hora_extra_diurna', 'hora_nocturna', 'hora_nocturna_extra', 'dominicales', 'dominicales_extras', 'dominincales_nocturnas', 'dominincales_nocturnas_extras']
		export_order = ['empleado', 'cedula', 'cargo', 'hora_diurna', 'hora_extra_diurna', 'hora_nocturna', 'hora_nocturna_extra', 'dominicales', 'dominicales_extras', 'dominincales_nocturnas', 'dominincales_nocturnas_extras']
	# end class
#end class

reports.register_export(Nomina, [NominaResource, NominaFResource, NominaDescResource, NominaResuResource])
reports.register_export(Turno, [TurnoResource])
