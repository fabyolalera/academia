from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'index.html', context={})


def contacto(request):
    if request.method == 'POST':
        contact_form = ContactoForm(request.POST)
        #print(request.POST)
        
        if(contact_form.is_valid()):
           # pass
            messages.success(request,'Gracias por contactarse.')
            #messages.info(request,'Otro mensajito')
        else:
            messages.warning(request,'Corrija los errores')
    else: 
        
        #context = {
            contact_form = ContactoForm() 
        #    }       
    return render(request, 'contacto.html', {'contact_form':contact_form},)


def galeria(request):
    return render(request, 'galeria.html', context={})

def nosotros(request):
    return render(request, 'nosotros.html', context={})