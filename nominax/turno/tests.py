# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import forms
import models

class TurnoTestCase(TestCase):
    def setUp(self):
    	self.form = forms.TurnoForm(intance=models.Turno.objects.get(pk=4))
    # end def

    def test_poner_horas(self):
    	self.form.poner_turno()
    # end def
# end class
