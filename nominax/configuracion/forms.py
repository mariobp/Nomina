# -*- coding: utf-8 -*-
from django import forms
import models


class ConfiguracionForm(forms.ModelForm):

    class Meta:
        model = models.Configuracion
        exclude = ()
    # end class

    @staticmethod
    def get_instance():
        instance = models.Configuracion.get_instance()
        if instance:
            return instance
        # end if
        raise forms.ValidationError('No se ha creado una configuración válida')
    # end def
# end class
