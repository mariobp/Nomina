# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from turno import forms as turnos
from recursos_h import forms as rec
import models
import decimal
from configuracion import forms as conf
from datetime import date, timedelta
from turno.datedelta import datedelta, multi_datedelta

class CorteForms(forms.ModelForm):
    class Meta:
        model = models.Corte
        exclude = ()
    # end class

    @staticmethod
    def get_instance():
        instance = models.Corte.get_instance()
        config = conf.ConfiguracionForm.get_instance()
        if not instance:
            instance = models.Corte()
            ultimo_corte = models.Corte.objects.all().order_by('fecha_inicio').last()
            if ultimo_corte:
            	instance.fecha_inicio = ultimo_corte.fecha_fin
            # end if
        # end if
        instance.prestaciones_sociales = config.prestaciones_sociales
        instance.nocturna = config.nocturna
        instance.dominical = config.dominical
        instance.nocturna_dominical = config.nocturna_dominical
        instance.descuento_salud = config.descuento_salud
        instance.extra_diurna = config.extra_diurna
        instance.extra_nocturna = config.extra_nocturna
        instance.extra_dominical_diurna = config.extra_dominical_diurna
        instance.extra_dominical_nocturna = config.extra_dominical_nocturna

        instance.save()
        return instance
    # end def
# end class

class NominaForm(forms.ModelForm):
    class Meta:
        model = models.Nomina
        exclude = ()
    # end class

    def clean_corte(self):
        if not 'corte' in self.cleaned_data or not self.cleaned_data['corte']:
            return CorteForms.get_instance()
        # end if
        return self.cleaned_data['corte']
    # end def

    def clean_contrato(self):
        if not 'contrato' in self.cleaned_data or not self.cleaned_data['contrato']:
            return rec.ContratoForm.get_instance(self.cleaned_data['empleado'])
        # end if
        return self.cleaned_data['contrato']
    # end def

    def clean(self):
    	if not self.cleaned_data['inicio_mes']:
    	    self.cleaned_data['inicio_mes'] = (self.cleaned_data['corte'].fecha_inicio).replace(day=1)
    	# end if
    	self.month = turnos.TurnoForm.month(self.cleaned_data['empleado'], self.cleaned_data['inicio_mes'].year, self.cleaned_data['inicio_mes'].month)
        self.turnos = turnos.TurnoForm.get_turnos(self.cleaned_data['corte'], self.cleaned_data['empleado'])
        if not self.turnos.count():
            raise forms.ValidationError('No hay turnos para este empleado')
        # end if
        return self.cleaned_data
    # end def

    @staticmethod
    def get_instance(empleado):
        corte = CorteForms.get_instance()
        instance = models.Nomina.objects.filter(empleado=empleado, corte=corte).first()
        if not instance:
            contrato = rec.ContratoForm.get_instance(empleado)
            instance = models.Nomina()
            instance.empleado = empleado
            instance.corte = corte
            instance.salario_base = contrato.salario_base
            instance.save()
        # end if
        return instance
    # end def

    def posibles_horas_extras(self):
        date_deltas = []
        for turn in self.month:
            date_deltas.append(datedelta(turn.entrada, turn.salida))
        # end for
        multi = multi_datedelta(date_deltas)
        multi2 = multi.move_to_hour(self.instance.contrato.horas_trabajo_corte)
        return multi2
    # end def

    def calcular_nomina(self, nomina):

        print 'calcular_nomina', len(self.turnos)

        today = nomina.corte.fecha_fin or date.today()
        delta = datedelta.for_dates(nomina.inicio_mes, today + timedelta(days=1))
        weeks = delta.timedelta().days / 7
        rango_extra = None
        if weeks >= 3:
            rango_extra = self.posibles_horas_extras()
        # end if
        deltas_diurno = multi_datedelta()
        deltas_nocturno = multi_datedelta()
        deltas_dominical_diurno = multi_datedelta()
        deltas_dominical_nocturno = multi_datedelta()
        
        for turno in self.turnos:
            deltas_diurno = deltas_diurno + turno.get_delta_diurna().difference(turno.get_delta_dominical())
            deltas_nocturno = deltas_nocturno + turno.get_delta_nocturna().difference(turno.get_delta_dominical())
            deltas_dominical_diurno = deltas_dominical_diurno + turno.get_delta_dominical().intersect(turno.get_delta_diurna())
            deltas_dominical_nocturno = deltas_dominical_nocturno + turno.get_delta_dominical().intersect(turno.get_delta_nocturna())
            
            print 'total: ', deltas_diurno.horas() + deltas_nocturno.horas() + deltas_dominical_diurno.horas() + deltas_dominical_nocturno.horas()
            print turno.entrada, turno.salida
            print deltas_diurno.horas()
            print deltas_nocturno.horas()
            print deltas_dominical_diurno.horas()
            print deltas_dominical_nocturno.horas()
        # end def

        nomina.hora_diurna = deltas_diurno.horas()
        print 'hora_diurna:', deltas_diurno.horas()
        nomina.horas_nocturna = deltas_nocturno.horas()
        nomina.horas_dominicales = deltas_dominical_diurno.horas() + deltas_dominical_nocturno.horas()

        if rango_extra:
            deltas_diurno_extra = deltas_diurno.intersect(rango_extra)
            deltas_nocturno_extra = deltas_nocturno.intersect(rango_extra)
            deltas_dominical_diurno_extra = deltas_dominical_diurno.intersect(rango_extra)
            deltas_dominical_nocturno_extra = deltas_dominical_nocturno.intersect(rango_extra)

            deltas_diurno = deltas_diurno.difference(deltas_diurno_extra)
            deltas_nocturno = deltas_nocturno.difference(deltas_nocturno_extra)
            deltas_dominical_diurno = deltas_dominical_diurno.difference(deltas_dominical_diurno_extra)
            deltas_dominical_nocturno = deltas_dominical_nocturno.difference(deltas_dominical_nocturno_extra)

            nomina.extras = deltas_diurno_extra.horas()
            nomina.extra_nocturna = deltas_nocturno_extra.horas()
            nomina.extra_dominical_diurna = deltas_dominical_diurno_extra.horas()
            nomina.extra_dominical_nocturna = deltas_dominical_nocturno_extra.horas()

        # end if

        nomina.dominical_diurna = deltas_dominical_diurno.horas()
        nomina.dominical_nocturna = deltas_dominical_nocturno.horas()
        nomina.nocturna = deltas_nocturno.horas()
        nomina.diurnas = deltas_diurno.horas()


    # end def

    def save(self, commit=True):
        nomina = super(NominaForm, self).save(commit)
        self.calcular_nomina(nomina)
        nomina.save()
        return nomina
    # end def
# end class


def cuando_apruebe(turno):
    nomina = NominaForm.get_instance(empleado = turno.empleado)
    #TODO aggregar campos y guardar formulario
    nom_form = NominaForm({'empleado': turno.empleado.pk, 'corte': nomina.corte.pk, 'salario_base': nomina.salario_base, 'inicio_mes': (nomina.corte.fecha_inicio).replace(day=1)}, instance = nomina)
    if nom_form.is_valid():
    	nom_form.save()
    else:
    	print nom_form.errors
    # end if
# end def
turnos.TurnoForm.cuando_apruebe = staticmethod(cuando_apruebe)