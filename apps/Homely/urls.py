from django.urls import path
from django.conf.urls import url
from .views.negocio import *
from .views.producto import *
#from .views.reseña import *
from .views.landing_page import landing_page

urlpatterns = [
    path('producto/', listarProductos, name = "listarProductos"),
    path('producto/<int:id>', verProducto, name = "verProducto"),
    path('producto/<int:id>/reseñas/', verReseñas, name = "verReseñas"),
    path('producto/crear/', crearProducto, name = "crearProducto"),
    path('producto/editar/<int:id>/', editarProducto, name = "editarProducto"),
    path('producto/eliminar/<int:id>/', eliminarProducto, name = "eliminarProducto"),

    path('negocio/', listarNegocios, name = "listarNegocios"),
    path('negocio/<int:id>', verNegocio, name = "verNegocio"),
]