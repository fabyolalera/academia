from django.contrib import admin
from django.urls import path
from ritmos.views import clases, lista_ritmos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clases/', clases, name='clases'),
    path('lista-ritmos/', lista_ritmos, name='lista_ritmos')
    
]
