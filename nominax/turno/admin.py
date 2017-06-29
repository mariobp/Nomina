# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

class DiaDominicalAdmin(admin.ModelAdmin):
	list_display = ['dia', 'proximo', 'anterior']

admin.site.register(models.Turno)
admin.site.register(models.DiaFestivo)
admin.site.register(models.DiaDominical, DiaDominicalAdmin)
