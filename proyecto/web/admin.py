from tkinter import Button
from django.contrib import admin
from .models import Cliente, Boleta, Sucursal
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "rut", "correo", "contraseña", "comentario"]

class BoletaAdmin(admin.ModelAdmin):
    list_display = ["folio", "rut_emisor", "rut_receptor", "tipo_servicio", "anio_doc", "mes_doc", "dia_doc", "comentario"]

class SucursalAdmin(admin.ModelAdmin):
    list_display = ["num_sucursal", "codigo", "nombre_unidad", "numero_cliente", "estado"]

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Boleta, BoletaAdmin)
admin.site.register(Sucursal, SucursalAdmin)