# -*- coding: utf-8 -*-
from django.db import models

class Asignatura(models,Model):
    nombre = models.CharField(max_length=25)
    def __str__(self):
        return self.nombre