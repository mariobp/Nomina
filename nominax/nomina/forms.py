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
        if not instance:
            instance = models.Corte()
            config = conf.get_instance()
            instance.nocturna = conf.nocturna
            instance.dominical = conf.dominical
            instance.nocturna_dominical = conf.nocturna_dominical
            instance.extra_diurna = conf.extra_diurna
            instance.extra_nocturna = conf.extra_nocturna
            instance.extra_dominical_diurna = conf.extra_dominical_diurna
            instance.extra_dominical_nocturna = conf.extra_dominical_nocturna

            instance.save()
        # end if
        return instance
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
        if not self.turnos.count():
            raise forms.ValidationError('No hay turnos paraeste empleado')
        # end if
        return self.cleaned_data
    # end def

    @staticmethod
    def get_instance(self, empleado):
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

    def calcular_nomina(self, nomina):
        horas_diurna = 0
        horas_nocturna = 0

        horas_extras = 0
        horas_dominicales = 0

        horas_extras_diurnas = 0
        horas_extras_nocturnas = 0

        horas_dominicales_diurnas = 0
        horas_dominicales_nocturnas = 0

        horas_dominicales_diurnas_extra = 0
        horas_dominicales_nocturnas_extra = 0


        for turno in self.turnos:
            horas_diurna = horas_diurna + turno.horas_diurna()
            horas_nocturna = horas_nocturna + turno.horas_nocturna()
    
            horas_extras = horas_extras + turno.horas_extras()
            horas_dominicales = horas_dominicales + turno.horas_dominical()
    
            horas_extras_diurnas = horas_extras_diurnas + turno.get_extras_diurnas()
            horas_extras_nocturnas = horas_extras_nocturnas + turno.get_extras_nocturnas()
    
            horas_dominicales_diurnas = horas_dominicales_diurnas + turno.get_dominicales_diurnas()
            horas_dominicales_nocturnas = horas_dominicales_nocturnas + turno.get_dominicales_nocturnas()
    
            horas_dominicales_diurnas_extra = horas_dominicales_diurnas_extra + turno.get_dominicales_diurnas_extra()
            horas_dominicales_nocturnas_extra = horas_dominicales_nocturnas_extra + turno.get_dominicales_nocturnas_extra()
        # end def

        nomina.extras = horas_extras_diurnas - horas_dominicales_diurnas_extra
        nomina.extra_nocturna = horas_extras_nocturnas - horas_dominicales_nocturnas_extra
        nomina.extra_dominical_diurna = horas_dominicales_diurnas_extra
        nomina.extra_dominical_nocturna = horas_dominicales_nocturnas_extra
        nomina.dominical_diurna = horas_dominicales_diurnas - horas_dominicales_diurnas_extra
        nomina.dominical_nocturna = horas_dominicales_nocturnas - horas_dominicales_nocturnas_extra
        nomina.nocturna = horas_nocturna - horas_dominicales_nocturnas - nomina.extra_nocturna
    # end def

    def save(self, commit=True):
        nomina = super(NominaForm, self).save(commit)
        self.calcular_nomina(nomina)
        nomina.save()
        return nomina
    # end def
# end class