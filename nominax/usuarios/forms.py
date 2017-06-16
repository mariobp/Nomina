# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios import models as usuarios


class MasterEdit(forms.ModelForm):

    def save(self, commit=False):
        master = super(MasterEdit, self).save(commit)
        if master.eliminado:
            user = CuserMiddleware.get_user()
            if user:
                master.eliminado_por = user
            # end if
        # end if
        master.save()
        return master
    # end def
# end class


class AsistenteForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(AsistenteForm, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
    # end def

    class Meta:
        model = usuarios.Asistente
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name',
                  'identificacion', 'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen']

# end class


class AsistenteFormEdit(MasterEdit):

    def __init__(self, *args, **kwargs):
        super(AsistenteFormEdit, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['fecha_nacimiento'].format = "m/d/y"
    # end def

    class Meta:
        model = usuarios.Asistente
        fields = ['username', 'email', 'first_name', 'last_name', 'identificacion',
                  'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen', 'eliminado']
    # end class
# end class


class AdministradorForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(AdministradorForm, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
    # end def

    class Meta:
        model = usuarios.Administrador
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name',
                  'identificacion', 'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen']

# end class


class AdministadorFormEdit(MasterEdit):

    def __init__(self, *args, **kwargs):
        super(AdministadorFormEdit, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['fecha_nacimiento'].format = "m/d/y"
    # end def

    class Meta:
        model = usuarios.Administrador
        fields = ['username', 'email', 'first_name', 'last_name', 'identificacion',
                  'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen', 'eliminado']
    # end class
# end class
