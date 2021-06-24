from django import forms
from django.forms import ModelForm, fields
from .models import UsuarioDonador,ingresoFundacion
 
class UsuarioDonadorForm(ModelForm):
    class Meta:
        model = UsuarioDonador
        fields = ['rut', 'nombre', 'apellido', 'email','nick','password','fecha_nacimiento','tipoUsuarioDonador','MedioPago']

class DonacionForm(ModelForm):
    class Meta:
        model = ingresoFundacion
        fields = ['MedioPago','NumeroTarjeta','monto','fecha_pago','UsuarioDonador']
                