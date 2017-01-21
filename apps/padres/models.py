# -*- coding: utf-8 -*-
from django.db import models
from apps.usuarios.models import Usuario

class Padre(models.Model):
    seleccionestado = (
        ('A', 'Soltero'),
        ('B', 'Casado'),
        ('C', 'Conviviente'),
        ('D', 'Viudo'),
        ('E', 'Divorsiado'),
    )
    estadocivil = models.CharField(max_length=1, choices=seleccionestado, default='A')
    seleccioninstruccion = (
        ('A', 'Primaria'),
        ('B', 'Secundaria'),
        ('C', 'Superior'),
        ('D', 'Post-Grado'),
    )
    instruccion = models.CharField(max_length=1, choices=seleccioninstruccion, default='A')
    actividad = models.CharField(max_length=100, null=True, blank=True)
    usuario = models.OneToOneField(Usuario)
    def __str__(self):
        return '%s %s' % (self.usuario.last_name, self.usuario.first_name)