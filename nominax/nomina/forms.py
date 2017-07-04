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
        config = conf.ConfiguracionForm.get_instance()
        if not instance:
            instance = models.Corte()
        # end if
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

    def __init__(self, *args, **kwargs):
    	super(NominaForm, self).__init__(*args, **kwargs)
    	self.fields['diurnas'].help_text = "%sx%d= $%s" % (str(self.instance.valor_hora()), self.instance.diurnas or 0, self.instance.calcular_hora_diurna(), ) 
    	self.fields['nocturna'].help_text = "%sx%dx%d%%= $%s" % (str(self.instance.valor_hora()), self.instance.nocturna or 0, self.instance.corte.nocturna, self.instance.calcular_hora_nocturna(), ) 
    	self.fields['extras'].help_text = "%sx%dx%d%%= $%s" % (str(self.instance.valor_hora()), self.instance.extras or 0, self.instance.corte.extra_diurna, self.instance.calcular_hora_extra_diurna(), ) 
    	self.fields['extra_nocturna'].help_text = "%sx%dx%d%%= $%s" % (str(self.instance.valor_hora()), self.instance.extra_nocturna or 0, self.instance.corte.extra_nocturna, self.instance.calcular_hora_extra_nocturna(), ) 
    	self.fields['dominical_diurna'].help_text = "%sx%dx%d%%= $%s" % (str(self.instance.valor_hora()), self.instance.dominical_diurna or 0, self.instance.corte.dominical, self.instance.calcular_hora_dominical_diurna(), ) 
    	self.fields['dominical_nocturna'].help_text = "%sx%dx%d%%= $%s" % (str(self.instance.valor_hora()), self.instance.dominical_nocturna or 0, self.instance.corte.nocturna_dominical, self.instance.calcular_hora_dominical_nocturna(), ) 
    	self.fields['extra_dominical_diurna'].help_text = "%sx%dx%d%%= $%s" % (str(self.instance.valor_hora()), self.instance.extra_dominical_diurna or 0, self.instance.corte.extra_dominical_diurna, self.instance.calcular_hora_dominical_extra_diurna(), ) 
    	self.fields['extra_dominical_nocturna'].help_text = "%sx%dx%d%%= $%s" % (str(self.instance.valor_hora()), self.instance.extra_dominical_nocturna or 0, self.instance.corte.extra_dominical_nocturna, self.instance.calcular_hora_dominical_extra_nocturna(), ) 

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

        print 'calcular_nomina', len(self.turnos)
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

        nomina.subsidio_trasporte = self.contrato.subsidio_transporte
        nomina.extras = horas_extras_diurnas - horas_dominicales_diurnas_extra
        nomina.extra_nocturna = horas_extras_nocturnas - horas_dominicales_nocturnas_extra
        nomina.extra_dominical_diurna = horas_dominicales_diurnas_extra
        nomina.extra_dominical_nocturna = horas_dominicales_nocturnas_extra
        nomina.dominical_diurna = horas_dominicales_diurnas - horas_dominicales_diurnas_extra
        nomina.dominical_nocturna = horas_dominicales_nocturnas - horas_dominicales_nocturnas_extra 
        nomina.nocturna = horas_nocturna - horas_dominicales_nocturnas - nomina.extra_nocturna

        nomina.horas_diurna = horas_diurna
        nomina.horas_nocturna = horas_nocturna
        nomina.horas_dominicales = horas_dominicales_diurnas + horas_dominicales_nocturnas

        print 'extras', nomina.extras
        print 'extra_nocturna', nomina.extra_nocturna
        print 'extra_dominical_diurna', nomina.extra_dominical_diurna
        print 'extra_dominical_nocturna', nomina.extra_dominical_nocturna
        print 'dominical_diurna', nomina.dominical_diurna
        print 'dominical_nocturna', nomina.dominical_nocturna
        print 'nocturna', nomina.nocturna
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
    nom_form = NominaForm({'empleado': turno.empleado.pk, 'corte': nomina.corte.pk, 'salario_base': nomina.salario_base}, instance = nomina)
    if nom_form.is_valid():
    	nom_form.save()
    else:
    	print nom_form.errors
    # end if
# end def
turnos.TurnoForm.cuando_apruebe = staticmethod(cuando_apruebe)