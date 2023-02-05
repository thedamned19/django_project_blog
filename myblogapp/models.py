from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(blank=False)
    contrasenia = models.TextField(max_length=50)
    nombre = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField(max_length=500)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)
    
    def __str__(self) :
        return self.titulo + " - " + self.subtitulo
    
class Avatar(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"


"""
class Imagen(models.Model):    
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.articulo}"
"""
