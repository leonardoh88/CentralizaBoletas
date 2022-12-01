from django import forms
from .models import Boleta,Sucursal



class BoletaForm(forms.ModelForm):
    
    class Meta:
        model = Boleta
        fields = ["comentario"]


class SucursalForm(forms.ModelForm):
    
    class Meta:
        model = Sucursal
        fields = ["comentario"]