from .models import Cliente, Boleta, Sucursal
from rest_framework import serializers


class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class BoletaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'


class SucursalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'