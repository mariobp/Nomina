# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from nominax.settings import ORIGIN
from supra import views as supra
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from cuser.middleware import CuserMiddleware
from nominax.decorator import check_login
import models
import json
import forms

from django.core import mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import urllib
import urllib2

from django.contrib.humanize.templatetags.humanize import intcomma

supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True


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
            if int(self.request.GET.get('num_page')) is 0:
                self.paginate_by = None
            else:
                self.paginate_by = self.request.GET.get('num_page', False)
            # end if
        # end if
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        eliminado = self.request.GET.get('eliminado', False)
        if eliminado == '1':
            queryset = queryset.filter(eliminado=True)
        else:
            queryset = queryset.filter(eliminado=False)
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

class SendMailSupraList(supra.SupraListView):
    model = models.Nomina
    subject = "ejemplo"
    sender = "exile"
    attach_name = "FINIQUITO.pdf"
    html = "hola!"
    url = "/admin/nomina/nomina/export/free/"
    list_filter=['corte']
    def get_queryset(self):
        queryset = super(SendMailSupraList, self).get_queryset()
        ids = self.request.GET.getlist('ids')
        queryset = queryset.filter(id__in=ids)
        for nom in queryset:
            if nom.contrato.empleado.email:
                values = { 'file_format': 0, }
                data = urllib.urlencode(values)
                req = urllib2.Request("http://"+self.request.get_host()+self.url + "?id=" + str(nom.id), data)
                response = urllib2.urlopen(req)
                result = response.read()

                msg = mail.EmailMultiAlternatives(self.subject, ".", self.sender, [nom.contrato.empleado.email])
                msg.attach_alternative(self.html, "text/html")
                msg.attach(self.attach_name, result, "application/pdf")
                msg.send()
            # end if
        # end for
        return queryset
    # end def
# end class

class NominaSupraList(supra.SupraListView):
    model = models.Nomina
    list_display = ['id', 'contrato__empleado', 'empleado_f', 'corte', 'corte_f', 'fecha', 'contrato__salario_base',
                    'contrato__subsidio_transporte', 'extras', 'extra_nocturna', 'extra_dominical_diurna',
                    'extra_dominical_nocturna', 'dominical_diurna', 'dominical_nocturna', 'nocturna',
                    'diurnas', 'dominical_diurna', 'dominical_nocturna',
                    'salario_produccion', 'descuento_salud', 'bonificacion', 'valor_hora', 'salario_legal', 'neto', 'total', 'recargos', 'total_pagar']
    search_fields = ['contrato__empleado__nombre', 'contrato__empleado__apellidos', 'contrato__empleado__cedula', ]
    list_filter = ['contrato__empleado', 'contrato__empleado__cargo', 'fecha', 'corte', 'id']
    search_key = 'q'
    paginate_by = 10

    def salario_produccion(self, obj, dict):
        return "$" + intcomma(round(obj.salario_produccion_nomina, 2))
    # end def

    def descuento_salud(self, obj, dict):
        return "$" + intcomma(round(obj.descuento_salud, 2))
    # end def

    def bonificacion(self, obj, dict):
        return "$" + intcomma(round(obj.bonificacion, 2))
    # end def

    def valor_hora(self, obj, dict):
        return "$" + intcomma(round(obj.valor_hora, 2))
    # end def

    def salario_legal(self, obj, dict):
        return "$" + intcomma(round(obj.total_devengado, 2))
    # end def

    def neto(self, obj, dict):
        return "$" + intcomma(round(obj.neto, 2))
    # end def

    def total(self, obj, dict):
        return "$" + intcomma(round(obj.total, 2))
    # end def

    def total_pagar(self, obj, dict):
        return "$" + intcomma(round(obj.total_pagar, 2))
    # end def

    def recargos(self, obj, dict):
        return "$" + intcomma(round(obj.recargos, 2))
    # end def


    def empleado_f(self, obj, now):
        return {"id": obj.contrato.empleado.id, "nombre": obj.contrato.empleado.nombre, "apellidos": obj.contrato.empleado.apellidos, "cedula": obj.contrato.empleado.cedula}
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
    list_display = ['id', 'empleado', 'empleado_f', 'corte', 'fecha', 'contrato__salario_base',
                    'contrato__subsidio_transporte', 'extras', 'extra_nocturna', 'extra_dominical_diurna',
                    'extra_dominical_nocturna', 'dominical_diurna', 'dominical_nocturna', 'nocturna',
                    'diurnas', 'dominical_diurna', 'dominical_nocturna']
    list_filter = ['empleado', 'empleado__cargo', 'fecha', 'corte', 'id']

    def empleado_f(self, obj, now):
        return {"id": obj.empleado.id, "nombre": obj.empleado.nombre, "apellidos": obj.empleado.apellidos, "cedula": obj.empleado.cedula}
    # end class
# end class

class CorteSupraList(supra.SupraListView):
    model = models.Corte
    list_display = ['id', 'fecha_inicio', 'fecha_fin', 'cerrado',
                    'nocturna', 'dominical', 'nocturna_dominical',
                    'extra_diurna', 'extra_nocturna' , 'extra_dominical_diurna',
                    'extra_dominical_nocturna']
    list_filter = ['id']

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


"""
    Descuento
"""

class DescuentoSupraList(MasterList):
    model = models.Descuento
    list_display = ['id', 'cantidad', 'contratos', 'corte', 'empleados']

    def get_queryset(self):
        queryset = super(DescuentoSupraList, self).get_queryset()
        corte = forms.CorteForms.get_instance()
        queryset = queryset.filter(corte = corte)
        return queryset
    # end def

    def empleados(self, obj, now):
        return obj.empleados()
    # end def

    def contratos(self, obj, now):
        lista = []
        for u in obj.contratos.all():
            lista.append(u.id)
        return lista
    # end def
# end class

class DescuentoSupraForm(supra.SupraFormView):
    model = models.Descuento
    form_class = forms.DescuentoForm

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(DescuentoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class DescuentoSupraFormDelete(supra.SupraDeleteView):
    model = models.Descuento


    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(DescuentoSupraFormDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class

"""
    DescuentoProduccion
"""

class DescuentoProduccionSupraList(MasterList):
    model = models.DescuentoProduccion
    list_display = ['id', 'fecha', 'corte', 'unidad', 'unidad__nombre','cantidad', 'concepto']

    def get_queryset(self):
        queryset = super(DescuentoProduccionSupraList, self).get_queryset()
        corte = forms.CorteForms.get_instance()
        queryset = queryset.filter(corte = corte)
        return queryset
    # end def

# end class

class DescuentoProduccionSupraForm(supra.SupraFormView):
    model = models.DescuentoProduccion
    form_class = forms.DescuentoProduccionForm

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(DescuentoProduccionSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class DescuentoProduccionSupraFormDelete(supra.SupraDeleteView):
    model = models.DescuentoProduccion


    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(DescuentoProduccionSupraFormDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class

class TipoIncapacidadSupraList(supra.SupraListView):
    model = models.TipoIncapacidad
    list_display = ['id', 'nombre']

# end class

class TipoIncapacidadSupraForm(supra.SupraFormView):
    model = models.TipoIncapacidad

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TipoIncapacidadSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class PagoIncapacidadSupraList(supra.SupraListView):
    model = models.PagoIncapacidad
    list_display = ['id', 'tipo', 'dia', 'porcentaje', 'tipo__nombre']

# end class

class PagoIncapacidadSupraForm(supra.SupraFormView):
    model = models.PagoIncapacidad

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(PagoIncapacidadSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class DiaIncapacidadSupraList(supra.SupraListView):
    model = models.DiaIncapacidad
    list_display = ['id', 'tipo', 'fecha', 'empleado', 'empleado__nombre', 'empleado__apellidos', 'dias','tipo__nombre',]

# end class

class DiaIncapacidadSupraForm(supra.SupraFormView):
    model = models.DiaIncapacidad

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(DiaIncapacidadSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class
