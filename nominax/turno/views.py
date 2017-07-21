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
from cuser.middleware import CuserMiddleware

supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE, OPTIONS"
supra.SupraConf.body = True
supra.SupraListView.datetime_format = '%d/%m/%Y %I:%M %p'


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

class TurnoSupraForm(supra.SupraFormView):
    model = models.Turno
    form_class = forms.TurnoForm
    list_display = ('id', 'empleado_id', 'empleado', 'entrada', 'salida', 'aprobado', 'creator', 'last_editor',)
    
    """
    def h_extras(self, obj, now):
        if hasattr(self, 'instance') and self.instance:
            return self.instance.horas_extras()
        return None
    # end def

    def h_nocturna(self, obj, now):
        if self.instance:
            return self.instance.horas_nocturna()
        return None
    # end def

    def h_diurna(self, obj, now):
        if self.instance:
            return self.instance.horas_diurna()
        return None
    # end def

    def h_dominical(self, obj, now):
        if self.instance:
            return self.instance.horas_dominical()
        return None
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
                    'entrada', 'salida', 'h_diurna','h_nocturna','h_extras', 'h_nocturna_extras',
                    'h_dominical','h_dominical_nocturna','h_dominical_extra','h_dominical_extra_nocturna', 'aprobado', 'creator', 'last_editor', 'descontar_almuerzo')
    search_fields = ['empleado__nombre', 'empleado__apellidos']
    list_filter = ['empleado', 'aprobado', 'id']

    def get_queryset(self):
        queryset = super(TurnoSupraList, self).get_queryset()
        queryset = queryset.filter(aprobado=False)
        return queryset
    # end def

    def h_extras(self, obj, now):
        return obj.horas_extras()
    # end def

    def h_nocturna(self, obj, now):
        return obj.horas_nocturna()
    # end def

    def h_diurna(self, obj, now):
        return obj.horas_diurna()
    # end def
    def h_nocturna_extras(self, obj, now):
        return obj.get_extras_nocturnas()
    #end def

    def h_dominical_nocturna(self, obj, now):
        return obj.get_dominicales_nocturnas()
    #end def

    def h_dominical(self, obj, now):
        return obj.horas_dominical()
    # end def

    def h_dominical_extra(self, obj, now):
        return obj.get_dominicales_diurnas_extra()
    # end def

    def h_dominical_extra_nocturna(self, obj, now):
        return obj.get_dominicales_nocturnas_extra()
    # end def
# end class

class TurnoSupraFormDelete(supra.SupraDeleteView):
    model = models.Turno

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TurnoSupraFormDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.aprobado:
            self.object.eliminado = True
            user = CuserMiddleware.get_user()
            self.object.eliminado_por = user
            self.object.save()
            return HttpResponse(status=200)
        # end if
        return HttpResponse(status=403)
    # end def
# end class

class ProduccionSupraList(MasterList):
    model = models.Produccion
    list_display = ['id', 'fecha', 'unidad', 'cantidad', 'unidad__nombre', 'empleados', 'concepto__nombre', 'cargo', 'cargo__nombre']
    search_fields = ['fecha', 'unidad', 'cantidad']

    def empleados(self, obj, now):
        lista = []
        for u in obj.empleados.all():
            lista.append(u.id)
        return lista
    # end def

    def cargo(self, obj, now):
        if obj.cargo():
            return obj.cargo().id
        #end if
        return None
    #end def

    def cargo__nombre(self, obj, now):
        if obj.cargo():
            return obj.cargo().nombre
        #end if
        return "Sin Cargo"
    #end def

# end class

class ProduccionSupraForm(supra.SupraFormView):
    model = models.Produccion
    form_class = forms.ProduccionForm

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.ProduccionFormEdit
        # end if
        return self.form_class
    # end class

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ProduccionSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class ProduccionSupraFormDelete(supra.SupraDeleteView):
    model = models.Produccion

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ProduccionSupraFormDelete, self).dispatch(request, *args, **kwargs)
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

def probar_turnos(request):
    if request.POST:
        form = forms.ProbarTurnos(request.POST)
        if form.is_valid():
            form.save()
        # end if
    else:
        form = forms.ProbarTurnos()
        return render('supra/form.html', {'form':form})
    # end def
# end def
