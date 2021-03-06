# -*- coding: utf-8 -*-
from django import forms
from configuracion import forms as conf
import models
from cuser.middleware import CuserMiddleware


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
        self.save_m2m()
        return master
    # end def
# end class


class TarifarioForm(forms.ModelForm):

    def save(self, commit=False):
        tarifa = super(TarifarioForm, self).save(commit)

        if not commit:
            tarifa.save()
        #end if

        if not tarifa.remplazado_por:
            remplazar = models.Tarifario.objects.filter(remplazado_por = None, unidad=tarifa.unidad, cargo=tarifa.cargo).last()
        # end if
        config = conf.ConfiguracionForm.get_instance()
        config.tarifario.remove(remplazar)
        config.tarifario.add(tarifa)
        tarifa.save()
        if not tarifa.remplazado_por:
            remplazar.remplazado_por = tarifa
            remplazar.save()
        # end if
        return tarifa
    # end def

    class Meta:
        model = models.Tarifario
        exclude = ['remplazado_por', 'eliminado_por']
    # end class
# end class


class CargoForm(forms.ModelForm):

    class Meta:
        model = models.Cargo
        fields = ['nombre', 'unidades_produccion']
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


class TipoContratoForm(forms.ModelForm):

    class Meta:
        model = models.TipoContrato
        fields = ['nombre', 'modalidad']
    # end class
# end class


class TipoContratoFormEdit(MasterEdit):

    class Meta:
        model = models.TipoContrato
        fields = ['nombre', 'modalidad']
    # end class
# end class

class BancoForm(forms.ModelForm):

    class Meta:
        model = models.Banco
        fields = ['nombre', 'codigo']
    # end class
# end class


class BancoFormEdit(MasterEdit):

    class Meta:
        model = models.Banco
        exclude = ('eliminado_por', )
    # end class
# end class

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = models.Empleado
        fields = ['nombre', 'apellidos', 'cedula', 'fecha_nacimiento', 'cargo', 'pension', 'eps', 'cesantia', 'cajacompensacion', 'banco', 'numero']
    # end class

    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['fecha_nacimiento'].format = "d/m/y"
    # end def
# end class


class ContratoForm(forms.ModelForm):

    class Meta:
        model = models.Contrato
        fields = ["empleado", 'fecha_inicio', 'salario_base', 'tipo_contrato', 'descanso_turno', 'inicio_descanso', 'fecha_finalizacion']
    # end class

    @staticmethod
    def get_instance(empleado, corte):
        instance = models.Contrato.get_instance(empleado, corte)
        if instance:
            return instance
        # end if
        raise forms.ValidationError("El empleado no tiene un contrato vigente")
    # end def

    def __init__(self, *args, **kwargs):
        super(ContratoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['fecha_inicio'].format = "d/m/y"
        self.fields['fecha_finalizacion'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['fecha_finalizacion'].format = "d/m/y"
    # end def
# end class

class UnidadProduccionForm(forms.ModelForm):

    class Meta:
        model = models.UnidadProduccion
        fields = ['nombre', ]
    # end class
# end class


class UnidadProduccionFormEdit(MasterEdit):

    class Meta:
        model = models.UnidadProduccion
        exclude = ('eliminado_por', )
    # end class
# end class
