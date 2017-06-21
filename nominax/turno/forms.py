# -*- coding: utf-8 -*-
from django import forms
import models
from cuser.middleware import CuserMiddleware


class TurnoForm(forms.ModelForm):

    class Meta:
        model = models.Turno
        exclude = ('aprobado_user', )
    # end class

    def save(self, commit=False):
        turno = super(TurnoForm, self).save(commit)
        if turno.aprobado:
            user = CuserMiddleware.get_user()
            if user:
                turno.aprobado_user = user
            # end if
        # end if
        turno.save()
        return turno
    # end def
# end class
