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

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True


def marcar_turno(request, pk):
    empleado = recursos_h.Empleado.objects.filter(pk=pk).first()
    if empleado:
        ultimo = models.Turno.objects.filter(empleado__pk=empleado.pk).order_by('pk').first()
        if ultimo is None or ultimo.salida is not None:
            turno = models.Turno()
            turno.entrada = timezone.now()
            turno.save()
        else:
            ultimo.salida = timezone.now()
            ultimo.save()
        # end if
    # end if
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
            self.paginate_by = self.request.GET.get('length', False)
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
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TurnoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class TurnoSupraList(MasterList):
    model = models.Turno
    list_display = ('id', 'empleado', 'empleado__nombre', 'empleado__apellidos',
                    'fecha', 'entrada', 'salida', 'extras', 'extra_nocturna', 'extra_diurna',
                    'extra_dominical', 'aprobado', 'creator', 'last_editor')
    search_fields = ['empleado__nombre', 'empleado__apellidos']
    list_filter = ['empleado', 'aprobado']
# end class
