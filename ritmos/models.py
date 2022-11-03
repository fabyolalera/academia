from distutils.command.upload import upload
from tabnanny import verbose

from turtle import width

from django.db import models


class Tipos_de_baile(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to = 'Ritmos', null=True) 
    
    def __str__(self):
        return self.nombre
    
    class Meta:    #Es que el panel del administrador se escriba en singular o plural
        verbose_name = 'Tipo de baile'
        verbose_name_plural = 'Tipos de bailes'
        
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    mensaje = models.CharField(max_length=300)
        