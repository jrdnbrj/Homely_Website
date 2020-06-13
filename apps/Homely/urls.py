from django.urls import path
from django.conf.urls import url
from .views.negocio import *
from .views.producto import *
from .views.reseña import *
from .views.promocion import *
from .views.pedido import *
from .views.reportes import *
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

    path('reseña/', listar_reseñas, name = "listar_reseñas"),
    path('reseña/crear/', crear_reseña, name = "crear_reseña"),
    path('reseña/editar/<int:id>/', editar_reseña, name = "editar_reseña"),
    path('reseña/eliminar/<int:id>/', eliminar_reseña, name = "eliminar_reseña"),

    path('promocion/', listar_promociones, name = "listar_promociones"),
    path('promocion/crear/', crear_promocion, name = "crear_promocion"),
    path('promocion/editar/<int:id>/', editar_promocion, name = "editar_promocion"),
    path('promocion/eliminar/<int:id>/', eliminar_promocion, name = "eliminar_promocion"),

    path('pedido/', listar_pedidos, name = "listar_pedidos"),
    path('pedido/crear/', crear_pedido, name = "crear_pedido"),
    path('pedido/editar/<int:id>/', editar_pedido, name = "editar_pedido"),
    path('pedido/eliminar/<int:id>/', eliminar_pedido, name = "eliminar_pedido"),

    path('reportes/', reportes, name='reportes'),
]