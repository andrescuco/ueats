import csv
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pedido
from .models import Usuario
from .models import Repartidor
from .models import Producto

# Clase que creara una vista API
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        default_items = [
            Pedido.objects.all().count(),
            Usuario.objects.all().count(),
            Producto.objects.all().count()]
        data = {
            "default": default_items,
        }
        return Response(data)

def index(request):
    pedidos = list(Pedido.objects.all().order_by('-id'))
    context = {'pedidos': pedidos}
    return render(request, 'reportes/index.html', context)

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

def exportar_pedidos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pedidos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Fecha', 'Cliente', 'Restaurante', 'Productos', 'Estado'])

    pedidos = Pedido.objects.all().values_list('fecha', 'usuario', 'restaurante', 'producto', 'estado')
    for pedido in pedidos:
        writer.writerow(pedido)

    return response
