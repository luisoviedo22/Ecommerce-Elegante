from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=30)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50, default="")
    talla = models.CharField(max_length=10, default="Null")
    color = models.CharField(max_length=20, default="Null")
    cantidad = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    estado = models.BooleanField(default=True)
    genero = models.CharField(max_length=10, default='hombre')
