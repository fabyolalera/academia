from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from academia.forms import ContactoForm   

def index(request):
    return render(request, 'index.html', context={})

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        print(request.POST)
        
    context = {
          'formulario' : ContactoForm()    
        }       
    return render(request, 'contacto.html', context=context)

def galeria(request):
    return render(request, 'galeria.html', context={})

def nosotros(request):
    return render(request, 'nosotros.html', context={})