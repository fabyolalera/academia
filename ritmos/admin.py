from re import T
from django.contrib import admin
from ritmos.models import Tipos_de_baile

#opcion 1 para registrar el modelo y que se vea en el panel de administrador
# admin.site.register(Tipos_de_baile)  

#SEGUNDA OPCION

@admin.register(Tipos_de_baile)
class Tipos_de_baile_admin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']  #aca tenemos que poner los nombres de los campos del models que queremos ver
    


