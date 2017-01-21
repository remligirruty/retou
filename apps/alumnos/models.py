# -*- coding: utf-8 -*-
from django.db import models

class Alumno(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=8, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    nickname = models.CharField(max_length=20, unique=True)
    seleccionsexo = (
        ('A', 'masculino'),
        ('B', 'femenino'),
    )
    sexo = models.CharField(max_length=1, choices=seleccionsexo, default='A')
    nacimiento = models.DateField('fecha de nacimiento', auto_now_add=False, null=True, blank=True)
    foto = models.ImageField(upload_to='static/fotos/medicos/', verbose_name=username, blank=True, null=True)
    registro = models.DateTimeField('fecha de registro', auto_now_add=True)
    seleccionarea = (
        ('A', 'Ingenieria'),
        ('B', 'Biomedicas'),
        ('C', 'Sociales'),
    )
    area = models.CharField(max_length=1, choices=seleccionarea, default='A')
    colegio = models.CharField(max_length=50, null=True)
    promocion = models.CharField(max_length=4, null=True)
    padre = models.ForeignKey(Padre)
    fin = models.DateField('fecha de final', auto_now_add=False, null=True, blank=True)
    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.first_name