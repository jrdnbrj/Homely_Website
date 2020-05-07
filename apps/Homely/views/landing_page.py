from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def landing_page(request):
    return render(request, 'index.html')

def registrar_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_verify = request.POST['password_verify']
        if password == password_verify:
            user = User.objects.create_user(username, email, password)
            if user is None:
                messages.error(request, 'Error al registrar usuario')
            return redirect('listarProductos')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
    return redirect('listarProductos')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Credenciales Incorrectas')
    return redirect('listarProductos')

def cerrar_sesion(request):
    logout(request)
    return redirect('/')