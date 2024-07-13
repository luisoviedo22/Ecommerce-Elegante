from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Producto
from django.contrib import messages

# Create your views here.


def add_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        genero = request.POST['genero']
        categoria = request.POST['categoria']
        talla = request.POST['talla']
        color = request.POST['color']
        cantidad = request.POST['cantidad']
        imagen = request.FILES.get('imagen')
        
        producto = Producto(
            nombre=nombre, 
            descripcion=descripcion, 
            precio=precio, 
            genero=genero,
            categoria=categoria, 
            talla=talla, 
            color=color,
            cantidad = cantidad,
            imagen=imagen
        )
        producto.save()
        messages.success(request, 'Producto agregado exitosamente.')
        return redirect('add_producto')
    
    return render(request, 'admin/add_products/add_producto.html')

def delete_producto(request, id):
    producto = Producto.objects.filter(id=id)
    producto.update(estado=False)
    messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('admin_productos')

def admin_productos(request):
    productos = Producto.objects.filter(estado=True)
    context = {'productos': productos}
    return render(request, 'admin/add_products/admin_productos.html', context)

def edit_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        genero = request.POST['genero']
        categoria = request.POST['categoria']
        talla = request.POST['talla']
        color = request.POST['color']
        cantidad = request.POST['cantidad']
        imagen = request.FILES.get('imagen', producto.imagen)
        
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.genero = genero
        producto.categoria = categoria
        producto.talla = talla
        producto.color = color
        producto.cantidad = cantidad
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

def catalogo(request):
    productos = Producto.objects.filter(estado=True)

    categoria = request.GET.get('categoria', '')
    talla = request.GET.get('talla', '')
    precio_max = request.GET.get('precio_max', '')

    if categoria:
        productos = productos.filter(categoria__iexact=categoria)
    if talla:
        productos = productos.filter(talla__iexact=talla)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    context = {
        'productos': productos
    }
    return render(request, 'users/productos/catalogo.html', context)

def productos_hombre(request):
    productos = Producto.objects.filter(genero='Hombre', estado=True)

    categoria = request.GET.get('categoria', '')
    talla = request.GET.get('talla', '')
    precio_max = request.GET.get('precio_max', '')

    if categoria:
        productos = productos.filter(categoria__iexact=categoria)
    if talla:
        productos = productos.filter(talla__iexact=talla)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    context = {
        'productos': productos
    }
    return render(request, 'users/productos/productos_hombre.html', context)

def productos_mujer(request):
    productos = Producto.objects.filter(genero='Mujer', estado=True)

    categoria = request.GET.get('categoria', '')
    talla = request.GET.get('talla', '')
    precio_max = request.GET.get('precio_max', '')

    if categoria:
        productos = productos.filter(categoria__iexact=categoria)
    if talla:
        productos = productos.filter(talla__iexact=talla)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    context = {
        'productos': productos
    }
    return render(request, 'users/productos/productos_mujer.html', context)

def productos_nino(request):
    productos = Producto.objects.filter(genero='Niño', estado=True)

    categoria = request.GET.get('categoria', '')
    talla = request.GET.get('talla', '')
    precio_max = request.GET.get('precio_max', '')

    if categoria:
        productos = productos.filter(categoria__iexact=categoria)
    if talla:
        productos = productos.filter(talla__iexact=talla)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    context = {
        'productos': productos
    }
    return render(request, 'users/productos/productos_nino.html', context)

def productos_nina(request):
    productos = Producto.objects.filter(genero='Niña', estado=True)

    categoria = request.GET.get('categoria', '')
    talla = request.GET.get('talla', '')
    precio_max = request.GET.get('precio_max', '')

    if categoria:
        productos = productos.filter(categoria__iexact=categoria)
    if talla:
        productos = productos.filter(talla__iexact=talla)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    context = {
        'productos': productos
    }
    return render(request, 'users/productos/productos_nina.html', context)

def view_product(request, id):
    producto = get_object_or_404(Producto, id=id)
    productos_relacionados = Producto.objects.filter(id=producto.id).exclude(id=producto.id)
    print(productos_relacionados)  # Agrega este print para verificar el contenido de la variable
    return render(request, 'users/productos/vista_producto.html', {'producto': producto, 'productos_relacionados': productos_relacionados})

