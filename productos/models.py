from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50, default="prenda")
    talla = models.CharField(max_length=10, default="Null")
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)