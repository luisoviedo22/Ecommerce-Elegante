from django.test import TestCase
from django.contrib.auth.models import User
from.models import Usuario, Profile

# Create your tests here.
# tests.py

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.usuario = Usuario.objects.create(
            primer_nombre='John',
            segundo_nombre='Doe',
            primer_apellido='Smith',
            segundo_apellido='Johnson',
            fecha_nacimiento='1990-01-01',
            imagen=None,
            correo='test@example.com',
            tipo_documento='CC',
            documento=123456,
            user=self.user,  # Asignar el objeto User creado previamente
            estado=True
        )

    def test_usuario_activo(self):
        self.assertTrue(self.usuario.estado)
        self.assertEqual(self.usuario.usuario_activo().count(), 1)
        self.assertTrue(self.usuario.estado)
        self.assertEqual(self.usuario.usuario_activo().count(), 1)

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.profile = Profile.objects.create(
            primer_nombre='Jane',
            segundo_nombre='Doe',
            primer_apellido='Smith',
            segundo_apellido='Johnson',
            fecha_nacimiento='1990-01-01',
            correo='test@example.com',
            tipo_documento='CC',
            documento=123456,
            user=self.user,  # Asignar el objeto User creado previamente
            estado=True
        )

class UserManagerTestCase(TestCase):
    def test_create_superuser(self):
        user = User.objects.create_superuser('testadmin', 'test@example.com', 'password')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testadmin')
        self.assertTrue(user.is_superuser)  # Verificar el campo is_superuser en lugar de is_admin