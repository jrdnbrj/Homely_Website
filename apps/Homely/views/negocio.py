from apps.Homely.models import Negocio, Producto
from apps.Homely.forms import NegocioForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/')
def verNegocios(request):
    negocios = Negocio.objects.all()
    contexto = {'negocios': negocios}
    return render(request, 'negocio/verNegocios.html', contexto)

def verNegocio(request, id):
    negocio = Negocio.objects.get(id = id)
    productos = Producto.objects.filter(negocio_id = id)
    contexto = {'negocio': negocio, 'productos': productos}
    return render(request, 'negocio/verNegocio.html', contexto)

@login_required(login_url = '/')
def listar_negocios(request):
    negocios = Negocio.objects.all()
    contexto = {'negocios': negocios}
    return render(request, 'negocio/listar_negocios.html', contexto)

@login_required(login_url = '/')
def crear_negocio(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = NegocioForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('listar_negocios')
        else:
            print(form.errors)
    else:
        form = NegocioForm()
    return render(request, 'negocio/crear_negocio.html', {'form': form, 'title': 'Crear'})


@login_required(login_url = '/')
def editar_negocio(request, id):
    negocio = Negocio.objects.get(id = id)
    if request.method == 'GET':
        form = NegocioForm(instance = negocio)
    else:
        form = NegocioForm(request.POST, request.FILES, instance = negocio)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('listar_negocios')
    return render(request, 'negocio/crear_negocio.html', {'form': form, 'title': 'Editar'})

@login_required(login_url = '/')
def eliminar_negocio(request, id):
    if request.method == 'POST':
        Negocio.objects.get(id = id).delete()
        return redirect('listar_negocios')
    return render(request, 'negocio/eliminar_negocio.html', {})