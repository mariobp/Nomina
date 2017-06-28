# -*- coding: utf-8 -*-
from django import forms
from configuracion import forms as conf
from recursos_h import forms as rec
import models
from cuser.middleware import CuserMiddleware
from datetime import datetime, date, time, timedelta

class datedelta():
    def __init__(self, start_date = None, end_date = None):
        self.start_date = start_date
        self.end_date = end_date
    # end def

    def daterange(self):
        car_date = self.start_date.date()
        end_date = self.end_date.date()
        while car_date <= end_date:
            yield car_date
            car_date = car_date + timedelta(days=1)
        # end for
    # end def

    def timedelta(self):
        if not self.empty():
            return self.end_date - self.start_date
        # end if
        return timedelta()
    # end def

    def empty(self):
        return not (self.start_date and self.end_date)
    # end def

    @staticmethod
    def for_day(single_date, start_date, end_date):
        return datedelta(datetime.combine(single_date, start_date), datetime.combine(single_date, end_date))
    # end def

    def low_date(self, date1, date2):
        return date1 if date1 < date2 else date2
    # end def

    def intersect(self, date_delta):
        if self.empty():
            return datedelta(date_delta.start_date, date_delta.end_date)
        elif date_delta.empty():
            return datedelta(self.start_date, self.end_date)
        elif self.end_date > date_delta.start_date and date_delta.start_date > self.start_date:
            return datedelta(date_delta.start_date, self.low_date(self.end_date, date_delta.end_date))
        elif date_delta.end_date > self.start_date and self.start_date > date_delta.start_date:
            return datedelta(self.start_date, self.low_date(self.end_date, date_delta.end_date))
        # end if
        return datedelta()
    # end def

    def difference_single(self, date_delta):
        if self.empty():
            return multi_datedelta()
        elif date_delta.empty():
            return multi_datedelta([datedelta(self.start_date, self.end_date)])
        elif self.end_date > date_delta.start_date and date_delta.start_date > self.start_date:
            delta = multi_datedelta([datedelta(self.start_date, date_delta.start_date)])
            if date_delta.end_date < self.end_date:
                delta = delta + datedelta(date_delta.end_date, self.end_date)
            # end if
            return delta
        elif date_delta.end_date > self.start_date and self.start_date > date_delta.start_date:
            if date_delta.end_date > self.end_date:
                return multi_datedelta()
            # end if
            return multi_datedelta([datedelta(date_delta.end_date, self.end_date)])
        # end if
        return multi_datedelta([datedelta(self.start_date, self.end_date)])
    # end def

    def difference(self, date_delta):
        if isinstance(date_delta, datedelta):
            return difference_single(date_delta)
        else:
            delta = multi_datedelta([datedelta(self.start_date, self.end_date)])
            return delta.difference(date_delta)
        # end if
    # end def


    def __str__(self):
        return "{%s - %s}" % (unicode(self.start_date), unicode(self.end_date))
    # end def
# end class

class multi_datedelta():

    def __init__(self, date_deltas = []):
        self.date_deltas = date_deltas
    # end def

    def __iter__(self):
        for single_delta in self.date_deltas:
            yield single_delta
        # end for
    # end def

    def break_datedelta(self, date_delta):
        pass
    # end def

    def difference_single(self, date_delta):
        multi_date_deltas = multi_datedelta()
        for single_dalta in self.date_deltas:
            delta = single_dalta.difference(date_delta)
            if not delta.empty():
                multi_date_deltas = multi_date_deltas + delta
            # end for
        # end for
        return multi_date_deltas
    # end def

    def intersect_single(self, date_delta):
        date_deltas = []
        for single_dalta in self.date_deltas:
            delta = date_delta.intersect(single_dalta)
            if not delta.empty():
                date_deltas.append(delta)
            # end for
        # end for
        return multi_datedelta(date_deltas)
    # end def

    def intersect_multi(self, multi_date_delta):
        multi_date_deltas = multi_datedelta()
        for single_dalta in self.date_deltas:
            multi_delta = multi_date_delta.intersect_single(single_dalta)
            if not delta.empty():
                multi_date_deltas = multi_date_deltas + multi_delta
            # end for
        # end for
        return multi_date_deltas
    # end def

    def difference_multi(self, multi_date_delta):
        multi_date_deltas = multi_datedelta(self.date_deltas)
        for single_dalta in multi_date_delta.date_deltas:
            multi_date_deltas = multi_date_delta.difference_single(single_dalta)
        # end for
        return multi_date_deltas
    # end def
    
    def difference_periodic(self, periodic_time_delta):
        multi_date_deltas = multi_datedelta(self.date_deltas)
        multi_date_deltas = periodic_time_delta.invert().intersect(multi_date_deltas)
        return multi_date_deltas
    # end def

    def intersect(self, date_delta):
        if isinstance(date_delta, datedelta):
            return self.intersect_single(date_delta)
        elif isinstance(date_delta, multi_datedelta):
            return self.intersect_multi(date_delta)
        # end if
        return multi_datedelta()
    # end def

    def difference(self, date_delta):
        if isinstance(date_delta, datedelta):
            return self.difference_single(date_delta)
        elif isinstance(date_delta, multi_datedelta):
            return self.difference_multi(date_delta)
        elif isinstance(date_delta, periodic_timedelta):
            return self.difference_periodic(date_delta)
        # end if
        return multi_datedelta()
    # end def

    def empty(self):
        return len(date_deltas) > 0
    # end if

    def __add__(self, date_delta):
        if isinstance(date_delta, datedelta):
            return multi_datedelta(self.date_deltas + [date_delta])
        elif isinstance(date_delta, multi_datedelta):
            return multi_datedelta(self.date_deltas + date_delta.date_deltas)
        # end if
        return None
    # end if

    def __str__(self):
        string = ""
        for single_delta in self.date_deltas:
            string = string + str(single_delta) + ", "
        # end for
        return "(%s)" % (string, )
    # end def

# end class

class periodic_timedelta():
    def __init__(self, start_time = None, end_time = None):
        self.start_time = start_time
        self.end_time   = end_time
    # end def

    def invert(self):
        return periodic_timedelta(self.end_time, self.start_time)
    # end def

    def intersec_by_day(self, single_date, date_delta):
        if self.start_time > self.end_time:
            delta1 = datedelta.for_day(single_date, time(0, 0, 0), self.end_time)
            delta2 = datedelta.for_day(single_date, self.start_time, time(23, 59, 59))
            delta = multi_datedelta([delta1, delta2])
        else:
            delta = multi_datedelta([datedelta.for_day(single_date, self.start_time, self.end_time)])
        # end if
        return delta.intersect(date_delta)
    # end def

    def intersect_single(self, date_delta):
        multi_date_delta = multi_datedelta()
        for single_date in date_delta.daterange():
            multi_date_delta = multi_date_delta + self.intersec_by_day(single_date, date_delta)
        # end for
        return multi_date_delta
    # end def

    def intersect_multi(self, multi_date_delta):
        multi_delta = multi_datedelta()
        for single_delta in multi_date_delta.date_deltas:
            multi_delta = multi_delta + self.intersect_single(single_delta)
        # end for
        return multi_delta
    # end def

    def intersect(self, date_delta):
        if isinstance(date_delta, datedelta):
            return self.intersect_single(date_delta)
        elif isinstance(date_delta, multi_datedelta):
            return self.intersect_multi(date_delta)
        # end if
        return multi_datedelta()
    # end def

    def __str__(self):
        return "[%s - %s]" % (self.start_time, self.end_time)
    # end def
# end def

class TurnoForm(forms.ModelForm):

    class Meta:
        model = models.Turno
        exclude = ('aprobado_user', )
    # end class

    def clean(self):

        self.configuracion = conf.ConfiguracionForm.get_instance()
        self.contrato = rec.ContratoForm.get_instance(self.cleaned_data['empleado'])
        if self.instance.aprobado:
            raise forms.ValidationError('El turno ya esta aprobado')
        # end if
        return self.cleaned_data
    # end def



    def poner_horas(self):
        h_recargo_nocturno_inicio = self.configuracion.h_recargo_nocturno_inicio
        h_recargo_nocturno_fin    = self.configuracion.h_recargo_nocturno_fin
        h_almuerzo_inicio = self.configuracion.h_almuerzo_inicio
        h_almuerzo_fin    = self.configuracion.h_almuerzo_fin

        instance = self.instance
        contrato = self.contrato

        fecha_hora_entrada = instance.entrada.replace(tzinfo=None)
        fecha_hora_salida = instance.salida.replace(tzinfo=None)

        fecha_extra_inicio = (fecha_hora_entrada + timedelta(hours = contrato.horas_trabajo))
        fecha_extra_fin = fecha_hora_salida

        nocturno = periodic_timedelta(h_recargo_nocturno_inicio, h_recargo_nocturno_fin)
        delta = datedelta(fecha_hora_entrada, fecha_hora_salida)
        delta_extra = datedelta(fecha_extra_inicio, fecha_extra_fin)
        almuerzo = periodic_timedelta(h_almuerzo_inicio, h_almuerzo_fin)

        print 'delta:', delta.difference(almuerzo)
        print 'nocturno:', nocturno
        print 'delta_extra:', delta_extra
        delta_nocturno = nocturno.intersect(delta)
        print 'delta_nocturno', delta_nocturno
        print 'delta_extra_nocturno', delta_nocturno.intersect(delta_extra)

    # end def

    def save(self, commit=False):
        turno = super(TurnoForm, self).save(commit)

        self.poner_horas()
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
