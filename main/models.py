from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length = 80)
    contenido = models.TextField()
    imagen = models.ImageField(default = "null",null = True)
    publico = models.BooleanField()
    creación = models.DateTimeField(auto_now_add = True)

class Categoria(models.Model):
    titulo = models.CharField(max_length = 80)
    descripcion = models.TextField()
    creación = models.DateTimeField(auto_now_add = True)
    
