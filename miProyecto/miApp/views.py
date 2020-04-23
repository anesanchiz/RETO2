from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Pedido, Productos, Cliente, Componente

#CLIENTES

#Devuelve los clientes ordenados por orden alf
#def index(request):
#    clientes = Cliente.objects.order_by('empresa')
#    output = ', '.join([d.empresa for d in clientes])
#    return HttpResponse(output)

def indexprod(request):
    productos = Productos.objects.order_by('referencia')
    context = {'lista_productos' : productos}
    return render(request, 'productos.html', context)

def index(request):
    clientes = Cliente.objects.order_by('empresa')
    context = {'lista_clientes' : clientes}
    return render(request, 'prueba.html', context)

#Devuelve los datos del cliente dado
def cliente(request, cliente_CIF):
    #clientes = Cliente.objects.get(pk=cliente_CIF)
    context = {
        'CIF':Cliente.objects.get(pk=cliente_CIF),
        'empresa': Cliente.objects.get(pk=cliente_CIF),
        'telefono':Cliente.objects.get(pk=cliente_CIF)
    }
    return render(request, 'base.html', context)

def componente(request, componente_codigo):
    componente = Componente.objects.get(pk=componente_codigo)
    return HttpResponse(componente)

def productos(request, productos_referencia):
    productos = Productos.objects.get(pk=productos_referencia)
    return HttpResponse(productos)

def pedido(request, pedido_codigo):
    pedido = Pedido.objects.get(pk=pedido_codigo)
    return HttpResponse(pedido)

