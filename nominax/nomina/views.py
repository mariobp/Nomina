# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from nominax.settings import ORIGIN
from supra import views as supra
from django.utils.decorators import method_decorator
from nominax.decorator import check_login
import models
# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True


class NominaSupraList(supra.SupraListView):
    model = models.Nomina
    list_display = ['id', 'empleado_f', 'corte_f', 'fecha', 'salario_base', 'subsidio_trasporte', 'extras', 'extra_nocturna', 'extra_diurna', 'extra_dominical', 'prestaciones_sociales', 'salario_produccion', 'bonificacion']
    search_fields = ['empleado__nombre', 'empleado__apellidos', 'empleado__cedula', ]
    list_filter = ['empleado', 'empleado__cargo', 'fecha']
    search_key = 'q'

    def empleado_f(self, obj, now):
        return {"id": obj.empleado.id, "nombre": obj.empleado.nombre, "apellidos": obj.empleado.apellidos, "cedula": obj.empleado.cedula}
    # end class

    def corte_f(self, obj, now):
        return {"id": obj.corte.id, "fecha_inicio": obj.corte.fecha_inicio.strftime("%Y-%m-%d"), "fecha_fin": obj.corte.fecha_fin.strftime("%Y-%m-%d")}
    # end def

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(NominaSupraList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(NominaSupraList, self).get_queryset()
        if self.request.GET.get('length', False):
            self.paginate_by = self.request.GET.get('length', False)
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
