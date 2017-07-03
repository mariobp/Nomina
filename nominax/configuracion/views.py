# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from nominax.settings import ORIGIN
from supra import views as supra
from django.utils.decorators import method_decorator
from nominax.decorator import check_login
from django.views.decorators.csrf import csrf_exempt
import models
import forms
# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True
supra.SupraConf.time_format = "%h:%M %p"


class ConfiguracionSupraList(supra.SupraListView):
    model = models.Configuracion
    list_display = ['id', 'tipo_corte', 'primer_dia', 'segundo_dia', 'h_recargo_nocturno_inicio', 'h_recargo_nocturno_fin',
                    'h_almuerzo_inicio', 'h_almuerzo_fin', 'extra_diurna', 'extra_nocturna', 'extra_dominical_diurna', 'extra_dominical_nocturna',
                    'nocturna', 'dominical', 'nocturna_dominical']

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(ConfiguracionSupraList, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class ConfiguracionSupraForm(supra.SupraFormView):
    model = models.Configuracion
    form_class = forms.ConfiguracionForm
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ConfiguracionSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class
