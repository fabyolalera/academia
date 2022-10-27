from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', context={})


def galeria(request):
    return render(request, 'galeria.html', context={})

def nosotros(request):
    return render(request, 'nosotros.html', context={})