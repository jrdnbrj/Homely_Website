from apps.Homely.models import Reseña
from apps.Homely.forms import ReseñaForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/')
def listar_reseñas(request):
    reseñas = Reseña.objects.all()
    contexto = {'reseñas': reseñas}
    return render(request, 'reseña/listar_reseñas.html', contexto)

@login_required(login_url = '/')
def crear_reseña(request):
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reseñas')
        else:
            print(form.errors)
    else:
        form = ReseñaForm()
    return render(request, 'reseña/crear_reseña.html', {'form': form, 'title': 'Crear'})


@login_required(login_url = '/')
def editar_reseña(request, id):
    reseña = Reseña.objects.get(id = id)
    if request.method == 'GET':
        form = ReseñaForm(instance = reseña)
    else:
        form = ReseñaForm(request.POST, instance = reseña)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('listar_reseñas')
    return render(request, 'reseña/crear_reseña.html', {'form': form, 'title': 'Editar'})

@login_required(login_url = '/')
def eliminar_reseña(request, id):
    if request.method == 'POST':
        Reseña.objects.get(id = id).delete()
        return redirect('listar_reseñas')
    return render(request, 'reseña/eliminar_reseña.html', {})