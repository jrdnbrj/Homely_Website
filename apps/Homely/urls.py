from django.urls import path
from django.conf.urls import url
from .views import *
from .views.landing_page import landing_page

urlpatterns = [
    path('', listarProductos, name = "listarProductos"),
    path('crear/', crearProducto, name = "crearProducto"),
    path('editar/<int:id>/', editarProducto, name = "editarProducto"),
    path('eliminar/<int:id>/', eliminarProducto, name = "eliminarProducto"),
]