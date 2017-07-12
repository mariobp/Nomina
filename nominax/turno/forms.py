# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from configuracion import forms as conf
from recursos_h import forms as rec
import models
from cuser.middleware import CuserMiddleware
from datedelta import datedelta, multi_datedelta, periodic_timedelta
from datetime import datetime, timedelta
from django.db import transaction


class TurnoForm(forms.ModelForm):

    class Meta:
        model = models.Turno
        fields = ['empleado', 'entrada', 'salida', 'aprobado']
    # end class

    @staticmethod
    def month(empleado, year, month):
        return models.Turno.month(empleado=empleado, year=year, month=month)
    # end def

    @staticmethod
    def get_turnos(corte, empleado):
        turnos = models.Turno.objects.filter(empleado=empleado, entrada__gte=corte.fecha_inicio, aprobado=True)
        if corte.fecha_fin:
            turnos = turnos.filter(entrada__lte=corte.fecha_fin)
        # end if
        return turnos.order_by('entrada')
    # end def

    @staticmethod
    def cuando_apruebe(turno):
        print 'no implementado'
    # end def

    @staticmethod
    def update_form(turno, data):
        class EditForm(TurnoForm):
            class Meta:
                model = models.Turno
                fields = ['empleado']
        # end class
        data['empleado'] = turno.empleado.pk
        form = EditForm(data, instance=turno)
        if form.is_valid():
            form.save()
            return form
        # end if
        print form.errors
        return form
    # end ef

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        return super(TurnoForm, self).post(request, *args, **kwargs)
    # end def

    def clean_salida(self):
        if self.cleaned_data['salida'] and self.cleaned_data['salida'] < self.cleaned_data['entrada']:
            raise forms.ValidationError('La salida no puede ir antes que la entrada')
        # end if
        return self.cleaned_data['salida']
    # end def

    def clean_empleado(self):
        return self.cleaned_data['empleado']
    # end def

    def clean(self):
        self.configuracion = conf.ConfiguracionForm.get_instance()
        # if self.instance.aprobado:
        #     raise forms.ValidationError('El turno ya esta aprobado')
        # end if
        return self.cleaned_data
    # end def

    def poner_horas(self, turno):
        h_recargo_nocturno_inicio = self.configuracion.h_recargo_nocturno_inicio
        h_recargo_nocturno_fin    = self.configuracion.h_recargo_nocturno_fin
        h_almuerzo_inicio = self.configuracion.h_almuerzo_inicio
        h_almuerzo_fin    = self.configuracion.h_almuerzo_fin

        instance = self.instance

        fecha_hora_entrada = instance.entrada.replace(tzinfo=None)
        fecha_hora_salida = instance.salida.replace(tzinfo=None)


        nocturno = periodic_timedelta(h_recargo_nocturno_inicio, h_recargo_nocturno_fin)
        delta = datedelta(fecha_hora_entrada, fecha_hora_salida)
        almuerzo = periodic_timedelta(h_almuerzo_inicio, h_almuerzo_fin)
        delta_dominicales = models.DiaDominical.multi_datedelta(delta)
        delta_festivos = models.DiaFestivo.multi_datedelta(delta)
        delta_dominicales_festivos = (delta_dominicales + delta_festivos).intersect(delta).difference(almuerzo)
        delta_dia = datedelta.for_day(fecha_hora_entrada.date(), datedelta.START_TIME, datedelta.END_TIME)
        delta_dominicales_festivos_dia = delta_dominicales_festivos.intersect(delta_dia)
        print delta_dominicales_festivos_dia
        delta_nocturno = nocturno.intersect(delta)
        delta_diurno = delta.difference(almuerzo).difference(nocturno)
        print 'delta_diurno:', delta.difference(almuerzo), delta_diurno, nocturno
        models.RangoFecha.objects.filter(extras=turno).delete()
        models.RangoFecha.objects.filter(nocturna=turno).delete()
        models.RangoFecha.objects.filter(diurna=turno).delete()
        models.RangoFecha.objects.filter(dominical=turno).delete()
        hasta_7 = datedelta(fecha_hora_entrada, (fecha_hora_entrada + timedelta(days=1)).replace(hour=7, minute=0, second=0) )

        for delta_single in delta_nocturno.date_deltas:
            nocturna = models.RangoFecha.create(delta_single.start_date, delta_single.end_date)
            turno.nocturna.add(nocturna)
        # end for

        for delta_single in delta_diurno.date_deltas:
            diurna = models.RangoFecha.create(delta_single.start_date, delta_single.end_date)
            turno.diurna.add(diurna)
        # end for

        if not delta_dominicales_festivos_dia.empty():
            for delta_single in hasta_7.difference(almuerzo).date_deltas:
                dominical = models.RangoFecha.create(delta_single.start_date, delta_single.end_date)
                turno.dominical.add(dominical)
            # end for
        # end if

    # end def

    def save(self, commit=False):
        turno = super(TurnoForm, self).save(commit)

        if turno.aprobado:
            user = CuserMiddleware.get_user()
            if user:
                turno.aprobado_user = user
            # end if
        # end if
        turno.save()
        print 'aprobado', turno.aprobado
        if turno.aprobado:
            print 'turno aprobado'
            TurnoForm.cuando_apruebe(turno)
        # end if
        if turno.salida:
            self.poner_horas(turno)
        # end if
        return turno
    # end def
# end class


class ProduccionForm(forms.ModelForm):

    class Meta:
        model = models.Produccion
        exclude = ('eliminado_por', )
    # end class
# end class


class ProduccionFormEdit(forms.ModelForm):
    
    class Meta:
        model = models.Produccion
        exclude = ('eliminado_por', )
    # end class

    def save(self, commit=False):
        master = super(ProduccionFormEdit, self).save(commit)
        if master.eliminado:
            user = CuserMiddleware.get_user()
            if user:
                master.eliminado_por = user
            # end if
        # end if
        master.save()
        self.save_m2m()
        return master
    # end def
# end class
