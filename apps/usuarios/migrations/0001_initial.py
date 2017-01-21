# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(max_length=8, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('sexo', models.CharField(max_length=1, default='A', choices=[('A', 'masculino'), ('B', 'femenino')])),
                ('nacimiento', models.DateField(verbose_name='fecha de nacimiento', blank=True, null=True)),
                ('foto', models.ImageField(verbose_name=models.CharField(max_length=8, unique=True), blank=True, null=True, upload_to='static/fotos/medicos/')),
                ('celular', models.CharField(max_length=9, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('registro', models.DateTimeField(verbose_name='fecha de registro', auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
