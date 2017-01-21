# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Padres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('estadocivil', models.CharField(max_length=1, default='A', choices=[('A', 'Soltero'), ('B', 'Casado'), ('C', 'Conviviente'), ('D', 'Viudo'), ('E', 'Divorsiado')])),
                ('instruccion', models.CharField(max_length=1, default='A', choices=[('A', 'Primaria'), ('B', 'Secundaria'), ('C', 'Superior'), ('D', 'Post-Grado')])),
                ('actividad', models.CharField(max_length=100, blank=True, null=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
