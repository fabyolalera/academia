from multiprocessing import context
from django.shortcuts import render
from ritmos.models import Tipos_de_baile

def clases(request):
    return render(request, 'clases.html', context={})

# def agregar_ritmo(request):
#     nuevo_ritmo = Tipos_de_baile.objects.create("")

def lista_ritmos(request):
    ritmos = Tipos_de_baile.objects.all()
    context = {
        'ritmos':ritmos
    }
    return render(request, 'ritmos/ritmos.html', context=context)