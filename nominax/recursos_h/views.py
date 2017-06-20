# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from nominax.settings import ORIGIN
from django.http import HttpResponse
from supra import views as supra
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from nominax.decorator import check_login
from cuser.middleware import CuserMiddleware
import models
import forms
# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True


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
    Cargos
"""


class CargoSupraList(MasterList):
    model = models.Cargo
    list_display = ['id', 'nombre']
    search_fields = ['nombre', ]
    paginate_by = 10
# end def


class CargoSupraForm(supra.SupraFormView):
    model = models.Cargo
    form_class = forms.CargoForm

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.CargoFormEdit
        # end if
        return self.form_class
    # end class

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CargoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class CargoSupraFormDelete(supra.SupraDeleteView):
    model = models.Cargo

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CargoSupraFormDelete, self).dispatch(request, *args, **kwargs)
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
    Pension
"""


class PensionSupraList(MasterList):
    model = models.Pension
    list_display = ['id', 'nombre', 'codigo']
    search_fields = ['nombre', 'codigo']
# end class


class PensionSupraForm(supra.SupraFormView):
    model = models.Pension
    form_class = forms.PensionForm

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.PensionFormEdit
        # end if
        return self.form_class
    # end class

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(PensionSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class PensionSupraFormDelete(supra.SupraDeleteView):
    model = models.Pension

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(PensionSupraFormDelete, self).dispatch(request, *args, **kwargs)
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
    Eps urls
"""


class EpsSupraList(MasterList):
    model = models.Eps
    list_display = ['id', 'nombre', 'codigo']
    search_fields = ['nombre', 'codigo']
# end class


class EpsSupraForm(supra.SupraFormView):
    model = models.Eps
    form_class = forms.EpsForm

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.EpsFormEdit
        # end if
        return self.form_class
    # end class

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(EpsSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class EpsSupraFormDelete(supra.SupraDeleteView):
    model = models.Eps

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(EpsSupraFormDelete, self).dispatch(request, *args, **kwargs)
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
