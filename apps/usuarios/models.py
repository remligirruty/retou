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

class Maestro(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=8, unique=True)
	email = models.EmailField(max_length=30, unique=True)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	seleccionsexo = (
		('A', 'masculino'),
		('B', 'femenino'),
	)
	sexo = models.CharField(max_length=1, choices=seleccionsexo, default='A')
	nacimiento = models.DateField('fecha de nacimiento', auto_now_add=False, null=True, blank=True)
	foto = models.ImageField(upload_to='static/fotos/medicos/', verbose_name=username, blank=True, null=True)
	celular = models.CharField(max_length=9, null=True)
	direccion = models.CharField(max_length=200, null=True)
	registro = models.DateTimeField('fecha de registro', auto_now_add=True)
	especialidad = models.CharField(max_length=25, null=True)
	
	objectsm = UserManager()

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.first_name

class Padre(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=8, unique=True)
	email = models.EmailField(max_length=30, unique=True)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	seleccionsexo = (
		('A', 'masculino'),
		('B', 'femenino'),
	)
	sexo = models.CharField(max_length=1, choices=seleccionsexo, default='A')
	nacimiento = models.DateField('fecha de nacimiento', auto_now_add=False, null=True, blank=True)
	foto = models.ImageField(upload_to='static/fotos/medicos/', verbose_name=username, blank=True, null=True)
	celular = models.CharField(max_length=9, null=True)
	direccion = models.CharField(max_length=200, null=True)
	registro = models.DateTimeField('fecha de registro', auto_now_add=True)
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
	actividad = models.CharField(max_length=100, null=True)

	objectsp = UserManager()

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.first_name

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
	objectsa = UserManager()

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.first_name