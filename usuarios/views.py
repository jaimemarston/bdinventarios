from django.shortcuts import render
from rest_framework import serializers, viewsets

from usuarios.models import Usuarios


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuarios.objects.all()
