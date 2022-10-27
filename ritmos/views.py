from multiprocessing import context
from django.shortcuts import render
from ritmos.models import Tipos_de_baile
from ritmos.forms import  ContactoForm

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        print(request.POST)
        
    context = {
          'formulario' : ContactoForm()    
        }       
    return render(request, 'contacto.html', context=context)

def agregar_ritmo(request):
    nuevo_ritmo = Tipos_de_baile.objects.create(nombre = 'Danza Española', descripcion = 'La danza española es una disciplina de la decada del 50')
    
    context = {
        'nuevo_ritmo':nuevo_ritmo
    }
    return render(request, 'ritmos/agregar_ritmo.html', context=context)

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