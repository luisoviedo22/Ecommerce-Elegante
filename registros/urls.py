"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from registros.views import *
from . import views

urlpatterns = [
    path("usuarios/", usuario_list_view, name="usuarios-listar"),
    path("usuarios/<int:id>/", usuario_list_view, name="usuarios-editar"),
    path("usuarios/eliminar/<int:id>/", usuario_delete_view, name="usuario-eliminar"),
    path('registrado/', views.header_register, name="registrado"),
    path('añadir/', views.add_products, name="añadir"),
    path('perfil/', views.perfil, name='perfil'),
    path('registros/register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registros/password-reset/', views.password_reset_confirm, name="reset-password"),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/actualizar/', views.actualizar_perfil, name='perfil-actualizar'),
]
