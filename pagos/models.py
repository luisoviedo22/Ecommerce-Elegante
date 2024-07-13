from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default='pendiente')

class Pago(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='pendiente')

class TarjetaUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(max_length=16)
    nombre_titular = models.CharField(max_length=100)
    fecha_expiracion = models.CharField(max_length=7)
    cvv = models.CharField(max_length=3)