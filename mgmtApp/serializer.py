from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cliente, Proyecto


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('idCliente', 'nombre', 'rubro', 'direccion', 'contacto')


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Proyecto
        fields = ('nombre', 'tipo', 'cliente', 'encargado')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')