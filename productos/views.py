from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.contrib import messages

# Create your views here.

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'users/productos/catalogo.html', {'productos': productos})

def add_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        talla = request.POST['talla']
        imagen = request.FILES.get('imagen')
        
        producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, categoria=categoria, talla=talla, imagen=imagen)
        producto.save()
        messages.success(request, 'Producto agregado exitosamente.')
        return redirect('add_producto')
    
    return render(request, 'admin/add_products/add_producto.html')

def delete_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('admin_productos')

def admin_productos(request):
    productos = Producto.objects.all()
    return render(request, 'admin/add_products/admin_productos.html', {'productos': productos})

def edit_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        talla = request.POST['talla']
        imagen = request.FILES.get('imagen', producto.imagen)
        
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.categoria = categoria
        producto.talla = talla
        producto.imagen = imagen
        producto.save()
        messages.success(request, 'Producto actualizado exitosamente.')
        return redirect('admin_productos')
    
    return render(request, 'admin/add_products/edit_producto.html', {'producto': producto})

def producto_list_view(request):
    productos = Producto.objects.all()
    context = {
        "productos": productos
    }
    return render(request, 'admin/productos/productos.html', context)

