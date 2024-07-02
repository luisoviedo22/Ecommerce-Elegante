from django.db import models

# Create your models here.

class productos:
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    precio = models.IntegerField(verbose_name="Precio")
    descripcion = models.CharField(max_length=50, verbose_name="Descripcion")
    