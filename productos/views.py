from django.shortcuts import render
from .models import Producto

# Create your views here.

def catalogo_view(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'users/productos/catalogo.html', context)
