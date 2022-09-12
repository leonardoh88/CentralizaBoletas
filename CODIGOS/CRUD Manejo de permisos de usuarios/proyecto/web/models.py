from datetime import date
from tkinter import commondialog
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=35)
    rut = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    correo = models.CharField(max_length=70)
    comentario= models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    codigo = models.CharField(max_length=100)
    fecha = models.DateField
    monto = models.IntegerField(max_length=200)
    tipo_consumo = models.CharField(max_length=30)
    rut = models.CharField(max_length=20)
    def __str__(self):
        return self.codigo


class Sucursal(models.Model):
    num_sucursal = models.IntegerField(max_length=4)
    codigo = models.CharField(max_length=10)
    nombre_unidad = models.CharField(max_length=70)
    numero_cliente = models.IntegerField(max_length=15)
    estado = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=4)
    zona = models.CharField(max_length=10)
    distribuidor = models.CharField(max_length=30)
    formato = models.CharField(max_length=20)
    def __str__(self):
        return self.num_sucursal



