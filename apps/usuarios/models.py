# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email es oligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, username, email, password = None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=8, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    # para todos
    seleccionsexo = (
        ('A', 'masculino'),
        ('B', 'femenino'),
    )
    sexo = models.CharField(max_length=1, choices=seleccionsexo, default='A')
    nacimiento = models.DateField('fecha de nacimiento', auto_now_add=False, null=True, blank=True)
    foto = models.ImageField(upload_to='static/fotos/medicos/', verbose_name=username, blank=True, null=True)
    celular = models.CharField(max_length=9, null=True)
    # cambiar a 250 y poner referencia
    direccion = models.CharField(max_length=200, null=True)
    registro = models.DateTimeField('fecha de registro', auto_now_add=True)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.first_name