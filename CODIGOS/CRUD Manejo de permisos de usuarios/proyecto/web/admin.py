from django.contrib import admin
from .models import Cliente, Boleta, Sucursal
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Boleta)
admin.site.register(Sucursal)