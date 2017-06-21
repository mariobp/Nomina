# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from nominax.settings import ORIGIN
from supra import views as supra
from recursos_h import models as recursos_h
import models
from django.utils import timezone

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True


def marcar_turno(request):
	empleado = request.GET.get('empleado', False)
	empleado = recursos_h.Empleado.objects.filter(pk=empleado).first()
	if empleado:
		ultimo = models.Turno.filter(empleado__pk=empleado.pk)
		if ultimo is None or ultimo.salida is not None:
			turno = models.Turno()
			turno.entrada = timezone.now()
			turno.save()
		else:
			ultimo.salida = timezone.now()
			ultimo.save()
		#end if
	#end if	
#end def