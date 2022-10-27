from unittest.util import _MAX_LENGTH
from django.db import models

class Tipos_de_baile(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(width_field=375, height_field=271)