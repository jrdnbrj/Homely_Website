from apps.Homely.models import Negocio, Producto
from apps.Homely.forms import NegocioForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/')
def listarNegocios(request):
    negocios = Negocio.objects.all()
    contexto = {'negocios': negocios}
    return render(request, 'negocio/listarNegocios.html', contexto)

def verNegocio(request, id):
    negocio = Negocio.objects.get(id = id)
    productos = Producto.objects.filter(negocio_id = id)
    contexto = {'negocio': negocio, 'productos': productos}
    return render(request, 'negocio/verNegocio.html', contexto)