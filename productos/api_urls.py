from django.urls import path
from . import api_views

urlpatterns = [
    path("productos/", api_views.producto_list, name="api_producto_list"),
    path("productos/<int:pk>/", api_views.producto_detail, name="api_producto_detail"),
    path("productos/<int:pk>/update/", api_views.producto_update, name="api_producto_update"),
    path("productos/<int:pk>/delete/", api_views.producto_delete, name="api_producto_delete"),
]
