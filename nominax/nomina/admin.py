# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms

class NominaAdmin(admin.ModelAdmin):
	form = forms.NominaForm
# end class

admin.site.register(models.Corte)
admin.site.register(models.Nomina, NominaAdmin)

