from apps.Homely.models import Pedido
from apps.Homely.forms import PedidoForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/')
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    contexto = {'pedidos': pedidos}
    return render(request, 'pedido/listar_pedidos.html', contexto)

@login_required(login_url = '/')
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedido/crear_pedido.html', {'form': form, 'title': 'Crear'})


@login_required(login_url = '/')
def editar_pedido(request, id):
    pedido = Pedido.objects.get(id = id)
    if request.method == 'GET':
        form = PedidoForm(instance = pedido)
    else:
        form = PedidoForm(request.POST, instance = pedido)
        if form.is_valid():
            form.save()
        return redirect('listar_pedidos')
    return render(request, 'pedido/crear_pedido.html', {'form': form, 'title': 'Editar'})

@login_required(login_url = '/')
def eliminar_pedido(request, id):
    if request.method == 'POST':
        Pedido.objects.get(id = id).delete()
        return redirect('listar_pedidos')
    return render(request, 'pedido/eliminar_pedido.html', {})