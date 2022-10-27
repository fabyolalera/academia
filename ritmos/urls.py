from django.contrib import admin
from django.urls import path
from ritmos.views import clases, lista_ritmos, contacto, agregar_ritmo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', contacto, name='contacto'),
    path('clases/', clases, name='clases'),
    path('agregar-ritmo', agregar_ritmo, name='agregar_ritmo'),
    path('lista-ritmos/', lista_ritmos, name='lista_ritmos'),
    
]
