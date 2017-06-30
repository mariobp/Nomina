# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from turno import forms as turnos
from configuracion import forms as conf
from recursos_h import forms as rec
import models
import decimal

class CorteForms(forms.ModelForm):
    class Meta:
        model = models.Corte
        exclude = ()
    # end class

    @staticmethod
    def get_instance():
        instance = models.Corte.get_instance()
        if instance:
            return instance
        # end if
        raise forms.ValidationError('No existe un corte actualemente vigente')
    # end def
# end class

class NominaForm(forms.ModelForm):
    class Meta:
        model = models.Nomina
        exclude = ()
    # end class

    def clean(self):
    	self.configuracion = conf.ConfiguracionForm.get_instance()
        self.contrato = rec.ContratoForm.get_instance(self.cleaned_data['empleado'])
        self.turnos = turnos.TurnoForm.get_turnos(self.cleaned_data['corte'], self.cleaned_data['empleado'])
        return self.cleaned_data
    # end def

    def calcular_nomina(self, nomina):
    	horas_diurna = 0
    	horas_nocturna = 0
        for turno in self.turnos:
            horas_diurna = horas_diurna + turno.horas_diurna()
            horas_nocturna = horas_nocturna + turno.horas_nocturna()
        # end def
        print 'Diurnas:', horas_diurna, decimal.Decimal(horas_diurna) * nomina.empleado.cargo.valor_hora_diurna
        print 'Nocturnas: ', horas_nocturna, decimal.Decimal(horas_nocturna) * nomina.empleado.cargo.valor_hora_nocturna
    # end def

    def save(self, commit=True):
        nomina = super(NominaForm, self).save(commit)
        self.calcular_nomina(nomina)
        nomina.save()
        return nomina
    # end def
# end class