from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cliente', views.ClienteViewsets)
router.register('boleta', views.BoletaViewsets)
router.register('sucursal', views.SucursalViewsets)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('boletas/', views.boletas, name='boletas'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('modificar/<id>/',views.modificar_boleta, name='modificar'),
    path('modiSucursal/<id>/',views.modificar_sucursal, name='modiSucursal'),
]