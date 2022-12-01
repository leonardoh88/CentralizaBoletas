from django.shortcuts import render, HttpResponse,get_object_or_404,redirect
from .models import Cliente, Boleta, Sucursal
from rest_framework import viewsets
from .serializers import ClienteSerializers, BoletaSerializers, SucursalSerializers
from .forms import BoletaForm,SucursalForm
# Create your views here.

class ClienteViewsets(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers

class BoletaViewsets(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializers

    def get_queryset(self):
        boletas = Boleta.objects.all()

        folio = self.request.GET.get('folio')

        if folio: 
            boletas = boletas.filter(folio__contains=folio)
        
        return boletas   

class SucursalViewsets(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializers



def index(request):
    return render(request,'Pagina/index.html')

def boletas(request):
    boletas = Boleta.objects.all()

    data = {
        'boletas': boletas
    }
    return render(request,'Pagina/boletas.html',data)

def logins(request):
    return render(request,'registration/login.html')


def modificar_boleta(request, id):

    boleta =get_object_or_404(Boleta, id=id)

    data = {
        'form': BoletaForm(instance=boleta)
    }

    if request.method == 'POST':
        formulariom = BoletaForm(data=request.POST, instance=boleta, files=request.FILES)
        if formulariom.is_valid():
            formulariom.save()
            return redirect(to='http://localhost:8000/boletas/')
        data["form"] = formulariom


    return render(request, 'Pagina/modificar.html', data)



def sucursales(request):
    sucursales = Sucursal.objects.all()

    data = {
        'sucursales': sucursales
    }
    return render(request,'Pagina/sucursales.html',data)


def modificar_sucursal(request, id):

    sucursal =get_object_or_404(Sucursal, id=id)

    data = {
        'form': SucursalForm(instance=sucursal)
    }

    if request.method == 'POST':
        formulariom = SucursalForm(data=request.POST, instance=sucursal, files=request.FILES)
        if formulariom.is_valid():
            formulariom.save()
            return redirect(to='http://localhost:8000/sucursales/')
        data["form"] = formulariom


    return render(request, 'Pagina/modiSucursal.html', data)

