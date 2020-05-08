from apps.Homely.models import Promocion
from apps.Homely.forms import PromocionForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/')
def listar_promociones(request):
    promociones = Promocion.objects.all()
    contexto = {'promociones': promociones}
    return render(request, 'promocion/listar_promociones.html', contexto)

@login_required(login_url = '/')
def crear_promocion(request):
    if request.method == 'POST':
        form = PromocionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_promociones')
    else:
        form = PromocionForm()
    return render(request, 'promocion/crear_promocion.html', {'form': form, 'title': 'Crear'})


@login_required(login_url = '/')
def editar_promocion(request, id):
    promocion = Promocion.objects.get(id = id)
    if request.method == 'GET':
        form = PromocionForm(instance = promocion)
    else:
        form = PromocionForm(request.POST, instance = promocion)
        if form.is_valid():
            form.save()
        return redirect('listar_promociones')
    return render(request, 'promocion/crear_promocion.html', {'form': form, 'title': 'Editar'})

@login_required(login_url = '/')
def eliminar_promocion(request, id):
    if request.method == 'POST':
        Promocion.objects.get(id = id).delete()
        return redirect('listar_promociones')
    return render(request, 'promocion/eliminar_promocion.html', {})