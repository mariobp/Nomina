#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @author: Exile
    @date: 05-07-2016
    @place: Cartagena - Colombia
    @licence: Creative Common
"""
from django.contrib import admin
from import_export.formats import base_formats
from import_export.admin import ExportMixin, ImportExportModelAdmin
from import_export import resources, fields
from plugins.pdf.format import PDF
from plugins.bancolombia.format import Bancolombia
from django.contrib.admin import site as admin_site
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from supra.views import access_control


class PdfExportMixin(ExportMixin):

    def export_action(self, request, rs, *args, **kwargs):
        self.resource_class = self.resource_classes[int(rs)]
        return super(PdfExportMixin, self).export_action(request, *args, **kwargs)
    #end def

    def get_export_formats(self,):
        formats = super(PdfExportMixin, self).get_export_formats()
        return [PDF, Bancolombia, base_formats.CSV, base_formats.XLSX]
    # end def
    def get_urls(self):
        urls = super(PdfExportMixin, self).get_urls()
        my_urls = [
            url(r'^export/free/(?P<rs>\d+)/$',
                csrf_exempt(access_control(self.export_action)),
                name='%s_%s_export' % self.get_model_info()),
        ]
        return my_urls + urls
    # end def
# end class


registry = {}

def register_export(model, resource_class):
	registry[model] = resource_class
# end def

old_register = admin_site.register

def register(model, *args, **kwargs):
    
    if model in registry:
    	if len(args):
    		modeladmin = args[0]
    	else:
    		modeladmin = admin.ModelAdmin
    	# end if
        class newadmin(PdfExportMixin, modeladmin):
            resource_classes = registry[model]
        # end class
        return old_register(model, newadmin)
    # end if
    return old_register(model, *args, **kwargs)
# end def


admin_site.register = register
