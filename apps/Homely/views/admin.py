from apps.Homely.models import *
from apps.Homely.forms import *
from django.shortcuts import render, redirect

def administrar(request):
    usuario = Usuario.__name__
    negocio = Negocio.__name__
    reseña = Reseña.__name__
    producto = Producto.__name__
    promocion = Promocion.__name__
    pedido = Pedido.__name__
    models = [usuario, negocio, reseña, producto, promocion, pedido]
    #models = [Usuario, Negocio, Reseña, Producto, Promocion, Pedido]
    contexto = {'models': models}
    return render(request, 'admin/admin.html', contexto)