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
	class Meta:
		model = Nomina
		fields = ['empleado__nombre']
	# end class

	#def export(self, queryset=None, *args, **kwargs):
	#	queryset = queryset.annotate(ventas=Count('buypresentation__buypoduct__sell__count')).order_by('-ventas')
	#	return super(ProductResource, self).export(queryset, *args, **kwargs)
	# end def
#end class
reports.register_export(Nomina, NominaResource)
