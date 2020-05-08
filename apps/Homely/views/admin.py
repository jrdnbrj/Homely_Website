from apps.Homely.models import *
from apps.Homely.forms import *
from django.shortcuts import render, redirect

def administrar(request):
    models = [Usuario.__name__, Negocio.__name__, Reseña.__name__, Producto.__name__, Promocion.__name__, Pedido.__name__]
    contexto = {'models': models}
    return render(request, 'admin/admin.html', contexto)

def administrar_tabla(request, model_name):
    if model_name == 'Usuario':
        return redirect('listarProductos')
    elif model_name == 'Negocio':
        return redirect('listar_negocios')
    elif model_name == 'Reseña':
        return redirect('listar_reseñas')
    elif model_name == 'Producto':
        return redirect('listarProductos')
    elif model_name == 'Promocion':
        return redirect('listarProductos')
    elif model_name == 'Pedido':
        return redirect('listarProductos')