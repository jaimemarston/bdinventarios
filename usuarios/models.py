import unicodedata
from django.contrib import admin
from django.db import models

from usuarios.manager import UserManager


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

    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    _password = None

    objects = UserManager()

    def get_username(self):
        """Return the identifying username for this User"""
        return getattr(self, self.USERNAME_FIELD)

    def __init__(self, *args, **kwargs):
        super(Usuarios, self).__init__(*args, **kwargs)
        # Stores the raw password if set_password() is called so that it can
        # be passed to password_changed() after the model is saved.
        self._password = None

    def __str__(self):
        return self.get_username()

    def clean(self):
        setattr(self, self.USERNAME_FIELD, self.normalize_username(self.get_username()))

    def natural_key(self):
        return (self.get_username(),)

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    @classmethod
    def get_email_field_name(cls):
        try:
            return cls.EMAIL_FIELD
        except AttributeError:
            return 'email'

    @classmethod
    def normalize_username(cls, username):
        return unicodedata.normalize('NFKC', username) if isinstance(username, str) else username

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
