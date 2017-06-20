# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from nominax.settings import ORIGIN
from supra import views as supra
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from nominax.decorator import check_login
from cuser.middleware import CuserMiddleware
import models
import forms
import json as simplejson
# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True


class LoginU(supra.SupraSession):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginU, self).dispatch(request, *args, **kwargs)
    # end def
# end class


@supra.access_control
def islogin(request):
    if request.user.is_authenticated():
        return HttpResponse(simplejson.dumps({"session": request.session.session_key, "username": request.user.username}), 200)
    # end if
    return HttpResponse([], 400)
# end if


class MasterList(supra.SupraListView):
    search_key = 'q'
    list_filter = ["id"]

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(MasterList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(MasterList, self).get_queryset()
        if self.request.GET.get('length', False):
            self.paginate_by = self.request.GET.get('length', False)
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


"""
    Servicios Asistente
"""


class AsistenteSupraForm(supra.SupraFormView):
    model = models.Asistente
    form_class = forms.AsistenteForm
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AsistenteSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.AsistenteFormEdit
        # end if
        return self.form_class
    # end class
# end class


class AsistenteSupraFormDelete(supra.SupraDeleteView):
    model = models.Asistente

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AsistenteSupraFormDelete, self).dispatch(request, *args, **kwargs)
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


class AsistenteList(MasterList):
    model = models.Asistente
    list_display = ['first_name', 'last_name', 'username', 'identificacion', 'date', 'email', 'direccion',
                    'telefono', 'fijo', 'creator', 'last_editor', 'imagen', 'id']
    search_fields = ['first_name', 'last_name',
                     'identificacion', 'email', 'username']
    paginate_by = 10

    def date(self, obj, row):
        return obj.fecha_nacimiento.strftime("%Y-%m-%d")
    # end def
# end class


"""
    Servicios Administrador
"""


class AdministradorSupraForm(supra.SupraFormView):
    model = models.Administrador
    form_class = forms.AdministradorForm
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AdministradorSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.AdministadorFormEdit
        # end if
        return self.form_class
    # end class
# end class


class AdministradorSupraFormDelete(supra.SupraDeleteView):
    model = models.Administrador

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AdministradorSupraFormDelete, self).dispatch(request, *args, **kwargs)
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


class AdministradorList(MasterList):
    model = models.Administrador
    list_display = ['first_name', 'last_name', 'username', 'identificacion', 'date', 'email', 'direccion',
                    'telefono', 'fijo', 'creator', 'last_editor', 'imagen', 'id']
    search_fields = ['first_name', 'last_name',
                     'identificacion', 'email', 'username']
    paginate_by = 10

    def date(self, obj, row):
        return obj.fecha_nacimiento.strftime("%Y-%m-%d")
    # end def
# end class
