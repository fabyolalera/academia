from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
<<<<<<< HEAD
from ritmos.forms import ContactoForm
=======

from academia.forms import ContactoForm   
>>>>>>> 944275e4f9f792a1444615beb9ad5fb93677c387

def index(request):
    return render(request, 'index.html', context={})


def contacto(request):
    if request.method == 'POST':
<<<<<<< HEAD
        formulario = ContactoForm(request.POST)
        #print(request.POST)
        
        if(formulario.is_valid()):
=======
        contact_form = ContactoForm(request.POST)
        #print(request.POST)
        
        if(contact_form.is_valid()):
>>>>>>> 944275e4f9f792a1444615beb9ad5fb93677c387
           # pass
            messages.success(request,'Gracias por contactarse.')
            #messages.info(request,'Otro mensajito')
        else:
            messages.warning(request,'Corrija los errores')
    else: 
        
        #context = {
<<<<<<< HEAD
            formulario = ContactoForm() 
        #    }       
    return render(request, 'contacto.html', {'formulario':formulario},)

=======
            contact_form = ContactoForm() 
        #    }       
    return render(request, 'contacto.html', {'contact_form':contact_form},)
>>>>>>> 944275e4f9f792a1444615beb9ad5fb93677c387

def galeria(request):
    return render(request, 'galeria.html', context={})

def nosotros(request):
    return render(request, 'nosotros.html', context={})