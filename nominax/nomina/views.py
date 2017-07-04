# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from nominax.settings import ORIGIN
from supra import views as supra
from django.utils.decorators import method_decorator
from nominax.decorator import check_login
import models
import json
# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True


class NominaSupraList(supra.SupraListView):
    model = models.Nomina
    list_display = ['id', 'empleado', 'empleado_f', 'corte', 'corte_f', 'fecha', 'salario_base',
                    'subsidio_trasporte', 'extras', 'extra_nocturna', 'extra_dominical_diurna',
                    'extra_dominical_nocturna', 'dominical_diurna', 'dominical_nocturna', 'nocturna',
                    'diurnas', 'dominical_diurna', 'dominical_nocturna', 'horas_diurna', 'horas_nocturna',
                    'horas_dominicales']
    search_fields = ['empleado__nombre', 'empleado__apellidos', 'empleado__cedula', ]
    list_filter = ['empleado', 'empleado__cargo', 'fecha', 'corte']
    search_key = 'q'
    paginate_by = 10

    def empleado_f(self, obj, now):
        return {"id": obj.empleado.id, "nombre": obj.empleado.nombre, "apellidos": obj.empleado.apellidos, "cedula": obj.empleado.cedula}
    # end class

    def corte_f(self, obj, now):
        if obj.corte.fecha_fin:
            fin = obj.corte.fecha_fin.strftime("%d/%m/%Y")
        else:
            fin = None
        # end if
        return {"id": obj.corte.id, "fecha_inicio": obj.corte.fecha_inicio.strftime("%d/%m/%Y"), "fecha_fin": fin}
    # end def

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(NominaSupraList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(NominaSupraList, self).get_queryset()
        if self.request.GET.get('num_page', False):
            self.paginate_by = self.request.GET.get('num_page', False)
        # end if
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        # end if
        if propiedad and orden:
            if orden == "asc":
                queryset = queryset.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-" + propiedad
                queryset = queryset.order_by(propiedad)
        # end if
        return queryset
    # end def
# end class


class NominaSupraList2(supra.SupraListView):
    model = models.Nomina
    list_display = ['id', 'empleado', 'empleado_f', 'corte', 'fecha', 'salario_base',
                    'subsidio_trasporte', 'extras', 'extra_nocturna', 'extra_dominical_diurna',
                    'extra_dominical_nocturna', 'dominical_diurna', 'dominical_nocturna', 'nocturna',
                    'diurnas', 'dominical_diurna', 'dominical_nocturna', 'horas_diurna', 'horas_nocturna',
                    'horas_dominicales']
    list_filter = ['empleado', 'empleado__cargo', 'fecha', 'corte']

    def empleado_f(self, obj, now):
        return {"id": obj.empleado.id, "nombre": obj.empleado.nombre, "apellidos": obj.empleado.apellidos, "cedula": obj.empleado.cedula}
    # end class
# end class


class CorteSupraList(supra.SupraListView):
    model = models.Corte
    list_display = ['fecha_inicio', 'fecha_fin', 'cerrado',
                    'nocturna', 'dominical', 'nocturna_dominical', 'prestaciones_sociales',
                    'extra_diurna', 'extra_nocturna' , 'extra_dominical_diurna',
                    'extra_dominical_nocturna', ('nominas', 'json')]

    def nominas(self, obj, now):
        class request():
            method = "GET"
            GET = {'corte': obj.pk}
        # end class
        lista = NominaSupraList2(dict_only=True).dispatch(request=request())
        return json.dumps(lista)
    # end def

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(CorteSupraList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(CorteSupraList, self).get_queryset()
        if self.request.GET.get('num_page', False):
            self.paginate_by = self.request.GET.get('num_page', False)
        # end if
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        # end if
        if propiedad and orden:
            if orden == "asc":
                queryset = queryset.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-" + propiedad
                queryset = queryset.order_by(propiedad)
        # end if
        return queryset
    # end def
# end class
