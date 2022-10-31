from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from ritmos.forms import ContactoForm

def index(request):
    return render(request, 'index.html', context={})


def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        #print(request.POST)
        
        if(formulario.is_valid()):
           # pass
            messages.success(request,'Gracias por contactarse.')
            #messages.info(request,'Otro mensajito')
        else:
            messages.warning(request,'Corrija los errores')
    else: 
        
        #context = {
            formulario = ContactoForm() 
        #    }       
    return render(request, 'contacto.html', {'formulario':formulario},)


def galeria(request):
    return render(request, 'galeria.html', context={})

def nosotros(request):
    return render(request, 'nosotros.html', context={})