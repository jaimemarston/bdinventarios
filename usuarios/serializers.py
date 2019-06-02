from rest_framework import serializers

from usuarios.models import Usuarios


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class AuthenticationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
