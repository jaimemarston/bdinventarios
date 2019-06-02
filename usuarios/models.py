from django.contrib import admin
from django.db import models


class Usuarios(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=200, null=True, blank=True)
    apellido_materno = models.CharField(max_length=200, null=True, blank=True)
    foto = models.ImageField(upload_to='usuarios', null=True, blank=True)
    sexo = models.IntegerField(null=True)
    correo = models.CharField(max_length=200, null=True, blank=True)
    telefono1 = models.CharField(max_length=50, null=True, blank=True)
    telefono2 = models.CharField(max_length=50, null=True, blank=True)
    role = models.ForeignKey('Roles', null=True, blank=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Roles(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.id, self.name)


@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    pass


@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    pass
