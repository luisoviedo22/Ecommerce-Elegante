from django.urls import path
from . import api_views


urlpatterns = [
    path("usuarios/", api_views.usuario_list, name="api_usuario_list")
]
