from multiprocessing import context
from tkinter.tix import Form

from django.shortcuts import redirect, render

from ritmos.forms import ContactoForm, Form_CrearClase
from ritmos.models import Contacto, Tipos_de_baile


def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        # print(request.POST)
        
        if formulario.is_valid():
            Contacto.objects.create(
                nombre = formulario.cleaned_data['nombre'],
                email = formulario.cleaned_data['email'],
                telefono = formulario.cleaned_data['telefono'],
                mensaje = formulario.cleaned_data['mensaje'],
            )
            
            # formulario.save()
    else:
        formulario = ContactoForm()
           
    context = {
          'formulario' : ContactoForm()    
        }       
   #return render(request, 'contacto.html', context=context)
    return render(request, 'contacto.html',{'formulario':formulario} )

def clases(request):
    ritmos = Tipos_de_baile.objects.all()
    context = {
        'ritmos': ritmos
    }
    return render(request, 'ritmos/clases.html', context=context)

def lista_ritmos(request):  #cumple la misma funcion que CLASES dado que traen todos los ritmos cargados en la base de datos
    lista_ritmos = Tipos_de_baile.objects.all()
    context = {
        'lista_ritmos':lista_ritmos
    }
    return render(request, 'ritmos/lista_ritmos.html', context=context)

def crear_clase(request): #agrefar dats en la base de dato de Tipo_de_baile
    if request.method == 'POST':
        form = Form_CrearClase(request.POST)
        
        if form.is_valid():
            Tipos_de_baile.objects.create(
                nombre= form.cleaned_data['nombre'],
                descripcion = form.cleaned_data['descripcion'],
                imagen = form.cleaned_data['imagen']
            )
            
        
        return redirect('clases')
    
    else:        
        context = {
            'crear_clase': Form_CrearClase()
        }
    return render(request, 'ritmos/crear_clase.html', context=context)