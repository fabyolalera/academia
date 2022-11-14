from distutils.command.upload import upload
from re import A
from socket import fromshare
from tkinter import Label
from unittest.util import _MAX_LENGTH

from django import forms
from django.forms import ValidationError

def alfabetico(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Ingrese un nombre que no contenga números:  %(valor)s',
                              #code='Error1',
                              params={'valor':value}
                              )


class ContactoForm(forms.Form):
    nombre = forms.CharField(
            label='Nombre',
            required=True,
            validators=(alfabetico,),
            error_messages={
                'required': 'Por favor ingrese un Nombre',
            },
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre (sólo texto)' })
            )
    
    email = forms.EmailField(
            label='Email',
            max_length=50,
            error_messages={
                'required': 'Por favor ingrese una dirección de correo',
                'invalid':'Por favor ingrese una dirección de mail válido'
            },
            widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Email'})
            )
    
    telefono = forms.IntegerField(
            label='Teléfono',
            max_value=100000000000,
            min_value=100000,
            error_messages={
                'required': 'Por favor ingrese un número de teléfono',
                'invalid':'Ingrese sólo números',
                'max_value':'No es un número válido',
                'min_value':'No es un número válido',
            },
            widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Telefono'})
            )
    
    mensaje = forms.CharField(
            label='Mensaje',
            max_length=150,
            error_messages={
                'required': 'Por favor ingrese un mensaje',
                'max_length':'Mensaje demasiado largo'
            },
            widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Mensaje','rows':5, 'cols':71})
            )
    
    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data
    
    
    def clean(self):
        cleaned_data = super().clean()
        #mensaje = cleaned_data.get("mensaje")
        #asunto = cleaned_data.get("asunto")

        #if "ayuda" not in  mensaje:
          #  msg = "Debe agregar la palabra 'ayuda' en el campo."
            #self.add_error('asunto', msg)
            #self.add_error('mensaje', msg)
        max_length=150,
        widget=forms.Textarea(attrs={'placeholder':'Mensaje','rows':5, 'cols':71})


class Form_CrearClase(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=500)
    imagen = forms.ImageField()
    

