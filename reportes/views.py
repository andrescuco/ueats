import csv
from django.shortcuts import render
from django.http import HttpResponse

from .models import Pedido
from .models import Usuario
from .models import Repartidor
from .models import Producto

def index(request):
    pedidos = list(Pedido.objects.all().order_by('-id'))
    context = {'pedidos': pedidos}
    return render(request, 'reportes/index.html', context)


def exportar_pedidos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pedidos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Fecha', 'Cliente', 'Restaurante', 'Productos', 'Estado'])

    pedidos = Pedido.objects.all().values_list('fecha', 'usuario', 'restaurante', 'producto', 'estado')
    for pedido in pedidos:
        writer.writerow(pedido)

    return response


def clientes(request):
    usuarios = list(Usuario.objects.all())
    context = {'usuarios': usuarios}
    return render(request, 'reportes/clientes.html', context)

def repartidores(request):
    repartidores = list(Repartidor.objects.all())
    context = {'repartidores': repartidores}
    return render(request, 'reportes/repartidores.html', context)

def productos(request):
    productos = list(Producto.objects.all())
    context = {'productos': productos}
    return render(request, 'reportes/productos.html', context)
