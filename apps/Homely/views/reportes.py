from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from apps.Homely.models import *
from apps.Homely.forms import *
from django.http import JsonResponse
from django.core import serializers

def reportes(request):
    if request.method == 'POST':
        reportes_dic = {
            0: default,
            1: restaurantes_ventas,
            2: productos_vendidos,
            3: productos_reseñas,
            4: usuarios_pedidos,
            5: restaurante_reseña,
        }
        opcion = int(request.POST['opcion'])
        funcion = reportes_dic[opcion]
        return funcion(request)
    return render(request, 'reportes/reportes.html', {})

def default(request):
    return JsonResponse(data={'response': {}}, safe=False)

def restaurantes_ventas(request):
    pedidos = Pedido.objects.all()
    negocios = Negocio.objects.all()
    response = {}
    venta = False
    cont = 0

    for negocio in negocios:
        for pedido in pedidos:
            for producto in pedido.productos.all():
                if producto.negocio == negocio:
                    venta = True
                    break
            if venta == True:
                cont = cont + 1
                venta = False
        response[negocio.nombre] = cont
        cont = 0
    response = {k: v for k, v in sorted(response.items(), key=lambda item: item[1], reverse=True)}
    print('response', response)
    return JsonResponse(data={'response': response}, safe=False)

def productos_vendidos(request):
    productos = Producto.objects.all().order_by('-numero_compras')
    response = {producto.nombre: producto.numero_compras for producto in productos}
    return JsonResponse(data={'response': response}, safe=False)

def productos_reseñas(request):
    productos = Producto.objects.all()
    productos = sorted(productos, key=lambda o:len(o.reseñas.all()), reverse=True)
    response = {producto.nombre: len(producto.reseñas.all()) for producto in productos}
    return JsonResponse(data={'response': response}, safe=False)

def usuarios_pedidos(request):
    response = {}
    cont = 0

    for usuario in Usuario.objects.all():
        for pedido in Pedido.objects.all():
            if pedido.usuario == usuario:
                cont = cont + 1
        response[usuario.username] = cont
        cont = 0

    response_sorted = sorted(response.items(), key=lambda item: item[1], reverse=True)
    response = {k: v for k, v in response_sorted}
    print('response', response)
    return JsonResponse(data={'response': response}, safe=False)

def restaurante_reseña(request):
    response = {}
    for negocio in Negocio.objects.all():
        suma, cont = 0, 0
        for producto in Producto.objects.filter(negocio = negocio):
            reseñas = [ reseña.calificacion for reseña in producto.reseñas.all() ]
            suma = suma + sum(reseñas)
            cont = cont + len(reseñas)
        try:
            response[negocio.nombre] = suma / cont
        except:
            response[negocio.nombre] = 0
    response_sorted = sorted(response.items(), key=lambda item: item[1], reverse=True)
    response = {k: v for k, v in response_sorted}
    print('response', response)
    return JsonResponse(data={'response': response}, safe=False)

def restaurante_fans(request):
    response = {}
    user = False
    for negocio in Negocio.objects.all():
        for usuario in Usuario.objects.all():
            suma, cont = 0, 0
            for producto in Producto.objects.filter(negocio = negocio):
                #reseñas = [ reseña for reseña in producto.reseñas.all() ]
                for reseña in producto.reseñas.all():
                    if reseña.usuario == usuario:
                        user = True
                        break
                if user == True:
                    break
            try:
                response[negocio.nombre] = suma / cont
            except:
                response[negocio.nombre] = 0
    response_sorted = sorted(response.items(), key=lambda item: item[1], reverse=True)
    response = {k: v for k, v in response_sorted}
    print('response', response)
    return JsonResponse(data={'response': response}, safe=False)

