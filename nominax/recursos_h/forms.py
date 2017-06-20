# -*- coding: utf-8 -*-
from django import forms
import models


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


class CargoForm(forms.ModelForm):

    class Meta:
        model = models.Cargo
        fields = ['nombre', ]
    # end class
# end class


class CargoFormEdit(MasterEdit):

    class Meta:
        model = models.Cargo
        exclude = ('eliminado_por', )
    # end class
# end class


class PensionForm(forms.ModelForm):

    class Meta:
        model = models.Pension
        fields = ['nombre', 'codigo']
    # end class
# end class


class PensionFormEdit(MasterEdit):

    class Meta:
        model = models.Pension
        exclude = ('eliminado_por', )
    # end class
# end class


class EpsForm(forms.ModelForm):

    class Meta:
        model = models.Eps
        fields = ['nombre', 'codigo']
    # end class
# end class


class EpsFormEdit(MasterEdit):

    class Meta:
        model = models.Eps
        exclude = ('eliminado_por', )
    # end class
# end class


class CajaForm(forms.ModelForm):

    class Meta:
        model = models.CajaCompensacion
        fields = ['nombre', 'codigo']
    # end class
# end class


class CajaFormEdit(MasterEdit):

    class Meta:
        model = models.CajaCompensacion
        exclude = ('eliminado_por', )
    # end class
# end class


class CesantiaForm(forms.ModelForm):

    class Meta:
        model = models.Cesantia
        fields = ['nombre', 'codigo']
    # end class
# end class


class CesantiaFormEdit(MasterEdit):

    class Meta:
        model = models.Cesantia
        exclude = ('eliminado_por', )
    # end class
# end class
