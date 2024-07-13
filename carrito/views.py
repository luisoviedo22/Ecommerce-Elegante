from django.http import JsonResponse
from django.shortcuts import render

from productos.models import Producto

# Create your views here.
def agregar_al_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = Producto.objects.get(id=producto_id)
        
        # Obtener el carrito de la sesión o crear uno nuevo
        carrito = request.session.get('carrito', [])
        
        # Agregar el producto al carrito
        carrito.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'imagen': producto.imagen.url,
            'cantidad': 1  # Puedes obtener la cantidad del formulario
        })
        
        # Guardar el carrito actualizado en la sesión
        request.session['carrito'] = carrito
        
        # Devolver una respuesta JSON con los productos del carrito
        return JsonResponse({'carrito': carrito})