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
import calendar

class CorteForms(forms.ModelForm):
    class Meta:
        model = models.Corte
        exclude = ()
    # end class

    @staticmethod
    def find_by_turn(turno):
        return models.Corte.objects.filter(fecha_inicio__lte=turno.entrada, fecha_fin__gte=turno.entrada).first()
    # end def

    @staticmethod
    def get_instance():
        instance = models.Corte.get_instance()
        config = conf.ConfiguracionForm.get_instance()
        if not instance:
            instance = models.Corte()
            ultimo_corte = models.Corte.objects.all().order_by('fecha_inicio').last()
            if ultimo_corte:
            	instance.fecha_inicio = ultimo_corte.fecha_fin + timedelta(days=1)
            # end if
        # end if
        if not instance.cerrado:
            instance.fecha_de_adelanto = instance.fecha_inicio.replace(day=config.primer_dia)
            rango = calendar.monthrange(instance.fecha_inicio.year, instance.fecha_inicio.month)

            instance.fecha_fin = instance.fecha_inicio.replace(day=config.segundo_dia if config.segundo_dia < rango[1] else rango[1])

            instance.nocturna = config.nocturna
            instance.dominical = config.dominical
            instance.nocturna_dominical = config.nocturna_dominical
            instance.salario_minimo_dia = config.salario_minimo_dia
            instance.descuento_salud = config.descuento_salud
            instance.extra_diurna = config.extra_diurna
            instance.extra_nocturna = config.extra_nocturna
            instance.extra_dominical_diurna = config.extra_dominical_diurna
            instance.extra_dominical_nocturna = config.extra_dominical_nocturna
        # end if

        instance.save()
        return instance
    # end def
# end class

class DescuentoForm(forms.ModelForm):
    class Meta:
        model = models.Descuento
        exclude = ()
    # end class

    def clean_corte(self):
        if not 'corte' in self.cleaned_data or not self.cleaned_data['corte']:
            return CorteForms.get_instance()
        # end if
        return self.cleaned_data['corte']
    # end def
# end class

class FinalizarDescuentoForm(forms.ModelForm):
    class Meta:
        model = models.Descuento
        fields = ['corte_final']
    # end class

    def clean_corte_final(self):
        if not 'corte_final' in self.cleaned_data or not self.cleaned_data['corte_final']:
            return CorteForms.get_instance()
        # end if
        return self.cleaned_data['corte_final']
    # end def
# end class

class DescuentoProduccionForm(forms.ModelForm):
    class Meta:
        model = models.DescuentoProduccion
        exclude = ()
    # end class

    def clean_corte(self):
        if not 'corte' in self.cleaned_data or not self.cleaned_data['corte']:
            return CorteForms.get_instance()
        # end if
        return self.cleaned_data['corte']
    # end def

# end class

class NominaForm(forms.ModelForm):
    turno = None

    class Meta:
        model = models.Nomina
        exclude = ()
    # end class

    def clean_corte(self):
        if not 'corte' in self.cleaned_data or not self.cleaned_data['corte']:
            if self.turno:
                corte = CorteForms.find_by_turn(self.turno)
                if corte:
                    return corte
                # end if
            # end if
            return CorteForms.get_instance()
        # end if
        return self.cleaned_data['corte']
    # end def

    def clean_contrato(self):
        self.month = turnos.TurnoForm.month(self.cleaned_data['contrato'].empleado, self.clean_inicio_mes().year, self.clean_inicio_mes().month)
        self.turnos = turnos.TurnoForm.get_turnos(self.clean_corte(), self.cleaned_data['contrato'].empleado)
        if not self.turnos.count():
            raise forms.ValidationError('No hay turnos para este empleado')
        # end if
        return self.cleaned_data['contrato']
    # end def

    def clean_inicio_mes(self):
        if not 'inicio_mes' in self.cleaned_data or not self.cleaned_data['inicio_mes']:
            return (self.clean_corte().fecha_inicio).replace(day=1)
        # end if
        return self.cleaned_data['inicio_mes']
    # end def

    @staticmethod
    def get_instance(empleado):
        corte = CorteForms.get_instance()
        instance = models.Nomina.objects.filter(contrato__empleado=empleado, corte=corte).first()
        contr = rec.ContratoForm.get_instance(empleado, corte)
        form = NominaForm({'contrato': contr.pk}, instance = instance)
        return form
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

        for turno in self.turnos.order_by('entrada'):
            deltas_diurno1 = turno.get_delta_diurna().difference(turno.get_delta_dominical())
            deltas_diurno = deltas_diurno + deltas_diurno1
            deltas_nocturno = deltas_nocturno + turno.get_delta_nocturna().difference(turno.get_delta_dominical())
            deltas_dominical_diurno = deltas_dominical_diurno + turno.get_delta_dominical().intersect(turno.get_delta_diurna())
            deltas_dominical_nocturno = deltas_dominical_nocturno + turno.get_delta_dominical().intersect(turno.get_delta_nocturna())
        # end def

        nomina.hora_diurna = deltas_diurno.horas()
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
    nom_form = NominaForm.get_instance(empleado = turno.empleado)
    nom_form.turno = turno
    if nom_form.is_valid():
    	nom_form.save()
    else:
    	raise Exception(nom_form.errors)
    # end if
# end def

turnos.TurnoForm.cuando_apruebe = staticmethod(cuando_apruebe)
