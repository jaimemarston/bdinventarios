from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=200, null=True, blank=True)
    apellido_materno = models.CharField(max_length=200, null=True, blank=True)
    foto = models.ImageField(upload_to='usuarios', null=True, blank=True)
    sexo = models.IntegerField(null=True)
    correo = models.CharField(max_length=200, null=True, blank=True)
    telefono1 = models.CharField(max_length=50, null=True, blank=True)
    telefono2 = models.CharField(max_length=50, null=True, blank=True)