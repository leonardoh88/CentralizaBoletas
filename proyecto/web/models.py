from operator import mod
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=35)
    rut = models.CharField(max_length=10)
    contraseña = models.CharField(max_length=20)
    correo = models.CharField(max_length=70)
    comentario= models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    folio = models.IntegerField()
    rut_emisor = models.CharField(max_length=10)
    rut_receptor = models.CharField(max_length=10)
    tipo_servicio = models.CharField(max_length=3)
    anio_doc = models.IntegerField()
    mes_doc = models.IntegerField()
    dia_doc = models.IntegerField()
    comentario = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.rut_emisor


class Sucursal(models.Model):
    num_sucursal = models.IntegerField()
    codigo = models.CharField(max_length=10)
    nombre_unidad = models.CharField(max_length=40)
    numero_cliente = models.CharField(max_length=15)
    estado = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)
    comuna = models.CharField(max_length=25)
    region = models.CharField(max_length=4)
    zona = models.CharField(max_length=10)
    distribuidor = models.CharField(max_length=25)
    formato = models.CharField(max_length=11)
    comentario = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.nombre_unidad


