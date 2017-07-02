# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from nominax.settings import ORIGIN
from supra import views as supra
from recursos_h import models as recursos_h
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from nominax.decorator import check_login
import models
import forms
from django.utils import timezone
from django.http import HttpResponse

supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True


def marcar_turno(request, pk):
    empleado = recursos_h.Empleado.objects.filter(pk=pk).first()
    if empleado:
        ultimo = models.Turno.objects.filter(empleado__pk=empleado.pk, salida = None).order_by('pk').first()
        if ultimo is None:
            turno = models.Turno()
            turno.entrada = timezone.now()
            turno.empleado = empleado
            turno.save()
        else:
            form = forms.TurnoForm({'salida': timezone.now().strftime('%Y-%m-%d %H:%M'), 'empleado': empleado.id, 'entrada': ultimo.entrada.strftime('%Y-%m-%d %H:%M')}, instance = ultimo)
            form.save()
        # end if
        return HttpResponse()
    # end if
    return HttpResponse(status=400)
# end def


class MasterList(supra.SupraListView):
    search_key = 'q'
    list_filter = ["id"]
    paginate_by = 10

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(MasterList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(MasterList, self).get_queryset()
        if self.request.GET.get('num_page', False):
            self.paginate_by = self.request.GET.get('num_page', False)
        # end if
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        eliminado = self.request.GET.get('aprobado', False)
        if eliminado == '1':
            queryset = queryset.filter(aprobado=True)
        else:
            queryset = queryset.filter(aprobado=False)
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


class TurnoSupraForm(supra.SupraFormView):
    model = models.Turno
    form_class = forms.TurnoForm
    list_display = ('id', 'empleado',
                    'entrada', 'salida', 'aprobado', 'creator', 'last_editor')
    """
    def h_extras(self, obj, now):
        return obj.horas_extras()
    # end def

    def h_nocturna(self, obj, now):
        return obj.horas_nocturna()
    # end def

    def h_diurna(self, obj, now):
        return obj.horas_diurna()
    # end def

    def h_dominical(self, obj, now):
        return obj.horas_dominical()
    # end def
    """

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TurnoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class TurnoSupraList(MasterList):
    model = models.Turno
    list_display = ('id', 'empleado', 'empleado__nombre', 'empleado__apellidos',
                    'entrada', 'salida', 'h_extras', 'h_nocturna', 'h_diurna',
                    'h_dominical', 'aprobado', 'creator', 'last_editor')
    search_fields = ['empleado__nombre', 'empleado__apellidos']
    list_filter = ['empleado', 'aprobado']

    def h_extras(self, obj, now):
        return obj.horas_extras()
    # end def

    def h_nocturna(self, obj, now):
        return obj.horas_nocturna()
    # end def

    def h_diurna(self, obj, now):
        return obj.horas_diurna()
    # end def

    def h_dominical(self, obj, now):
        return obj.horas_dominical()
    # end def
# end class
