from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from django.forms.widgets import PasswordInput

from usuarios.models import User
from .models import User

# from para agregar usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['estatura','peso', 'imagen', 'telefono',
                    'grado', 'curp', 'direccion', 'cedula','matricula']
        labels = {'estatura:Estatura' ,
                    'peso:Peso',
                    'imagen:Imagen',    
                    'telefonoTelefono:',
                    'grado:Grado',
                    'curp:Crup',
                    'direccion:Dirección',
                    'cedula;Cedula',
                    'matricula:Matricula'}