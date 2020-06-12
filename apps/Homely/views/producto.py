from apps.Homely.models import Producto, Reseña
from apps.Homely.forms import ProductoForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/')
def listarProductos(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'producto/listarProductos.html', contexto)

def verProducto(request, id):
    producto = Producto.objects.get(id = id)
    contexto = {'producto': producto}
    return render(request, 'producto/verProducto.html', contexto)

@login_required(login_url = '/')
def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarProductos')
        else:
            print(form.errors)
    else:
        form = ProductoForm()
    return render(request, 'Producto/crearProducto.html', {'form': form, 'title': 'Crear'})


@login_required(login_url = '/')
def editarProducto(request, id):
    producto = Producto.objects.get(id = id)
    if request.method == 'GET':
        form = ProductoForm(instance = producto)
    else:
        form = ProductoForm(request.POST, request.FILES, instance = producto)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('listarProductos')
    return render(request, 'Producto/crearProducto.html', {'form': form, 'title': 'Editar'})

@login_required(login_url = '/')
def eliminarProducto(request, id):
    if request.method == 'POST':
        Producto.objects.get(id = id).delete()
        return redirect('listarProductos')
    return render(request, 'Producto/eliminarProducto.html', {})

def verReseñas(request, id):
    producto = Producto.objects.get(id = id)
    contexto = {'producto': producto}
    return render(request, 'producto/verReseñas.html', contexto)