# -*- coding: utf-8 -*-
from django.db import models
from apps.usuarios.models import Usuario

class Asignatura(models,Model):
    nombre = models.CharField(max_length=25)
    def __str__(self):
        return self.nombre

class Maestro(models.Model):
    username = models.CharField(max_length=25, blank=True, null=True)
    asignatura = ForeignKey(Asignatura)
    usuario = models.OneToOneField(Usuario)
    def __str__(self):
        return '%s %s' % (self.usuario.last_name, self.asignatura.nombre)