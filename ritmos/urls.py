from django.contrib import admin
from django.urls import path
from ritmos.views import clases, lista_ritmos, contacto, crear_clase

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', contacto, name='contacto'),
    path('clases/', clases, name='clases'),
    path('lista-ritmos/', lista_ritmos, name='lista_ritmos'),
    path('crear-clase/', crear_clase, name='crear_clase')
    
]
