from django.urls import path
from django.conf.urls import url
from .views.negocio import *
from .views.producto import *
#from .views.reseña import *
from .views.landing_page import landing_page

urlpatterns = [
    path('productos/', listarProductos, name = "listarProductos"),
    path('producto/<int:id>', verProducto, name = "verProducto"),
    path('producto/<int:id>/reseñas/', verReseñas, name = "verReseñas"),
    path('producto/crear/', crearProducto, name = "crearProducto"),
    path('producto/editar/<int:id>/', editarProducto, name = "editarProducto"),
    path('producto/eliminar/<int:id>/', eliminarProducto, name = "eliminarProducto"),

    path('negocio/', verNegocios, name = "verNegocios"),
    path('negocio/<int:id>', verNegocio, name = "verNegocio"),

    path('negocios/', listar_negocios, name = "listar_negocios"),
    path('negocio/crear/', crear_negocio, name = "crear_negocio"),
    path('negocio/editar/<int:id>/', editar_negocio, name = "editar_negocio"),
    path('negocio/eliminar/<int:id>/', eliminar_negocio, name = "eliminar_negocio"),
]