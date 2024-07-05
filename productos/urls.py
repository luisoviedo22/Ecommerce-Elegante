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
from . import views

urlpatterns = [
    path('catalogo/', views.catalogo, name="catalogo"),
    path('admin/productos/add/', views.add_producto, name='add_producto'),
    path('admin/productos/delete/<int:producto_id>/', views.delete_producto, name='delete_producto'),
    path('admin/productos/', views.admin_productos, name='admin_productos'),
    path('admin/productos/edit/<int:producto_id>/', views.edit_producto, name='edit_producto'),
]
