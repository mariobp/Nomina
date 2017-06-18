# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from cuser.fields import CurrentUserField

# Create your models here.


class Administrador(User):
    identificacion = models.CharField(
        max_length=120, verbose_name="Identificación", unique=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    direccion = models.CharField(max_length=120, blank=True, null=True)
    telefono = models.CharField(
        max_length=15, verbose_name="Teléfono", blank=True, null=True)
    fijo = models.CharField(
        max_length=15, verbose_name="Fijo", blank=True, null=True)
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)
    creator = CurrentUserField(add_only=True, related_name="created_administrador")
    last_editor = CurrentUserField(related_name="last_edited_administrador")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_administrador", blank=True, null=True)

    class Meta:
        verbose_name = "Asistente"
        verbose_name_plural = "Asistentes"
    # end class

    def avatar(self):
        if self.imagen:
            imagen = self.imagen
        else:
            imagen = 'account.svg'
        # end if
        return '<img class="image-cicle" src="/media/%s" />' % (imagen)
    # end def

    avatar.allow_tags = True

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def
# end class


class Asistente(User):
    identificacion = models.CharField(
        max_length=120, verbose_name="Identificación", unique=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    direccion = models.CharField(max_length=120, blank=True, null=True)
    telefono = models.CharField(
        max_length=15, verbose_name="Teléfono", blank=True, null=True)
    fijo = models.CharField(
        max_length=15, verbose_name="Fijo", blank=True, null=True)
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)
    creator = CurrentUserField(add_only=True, related_name="created_asistente")
    last_editor = CurrentUserField(related_name="last_edited_asistente")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_asistente", blank=True, null=True)

    class Meta:
        verbose_name = "Asistente"
        verbose_name_plural = "Asistentes"
    # end class

    def avatar(self):
        if self.imagen:
            imagen = self.imagen
        else:
            imagen = 'account.svg'
        # end if
        return '<img class="image-cicle" src="/media/%s" />' % (imagen)
    # end def

    avatar.allow_tags = True

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def
# end class
