from django.forms import ValidationError
from django.test import TestCase
from .models import Producto

class ProductoTestCase(TestCase):
    def test_producto_nombre_vacio(self):
        # Intentar crear un producto con nombre vacío
        producto = Producto(
            nombre="",
            descripcion="Descripción del producto",
            precio=19.99,
            categoria="Electrónica",
            talla="M",
            color="Azul",
            cantidad=10,
            imagen=None,
            estado=True,
            genero="hombre"
        )
        with self.assertRaises(ValidationError):
            producto.full_clean()

    def test_producto_precio_negativo(self):
        # Intentar crear un producto con precio negativo
        producto = Producto(
            nombre="Producto de prueba",
            descripcion="Descripción del producto",
            precio=-19.99,
            categoria="Electrónica",
            talla="M",
            color="Azul",
            cantidad=10,
            imagen=None,
            estado=True,
            genero="hombre"
        )
        with self.assertRaises(ValidationError):
            producto.full_clean()

    def test_producto_categoria_vacia(self):
        # Intentar crear un producto con categoría vacía
        producto = Producto(
            nombre="Producto de prueba",
            descripcion="Descripción del producto",
            precio=19.99,
            categoria="",
            talla="M",
            color="Azul",
            cantidad=10,
            imagen=None,
            estado=True,
            genero="hombre"
        )
        with self.assertRaises(ValidationError):
            producto.full_clean()