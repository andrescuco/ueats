from datetime import datetime
from datetime import timedelta
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import DetailView

from .models import Pedido
from .models import Usuario
from .models import Repartidor
from .models import Producto
from .models import Restaurante
from .models import Reclamo

import csv

# Vista basada en clase generica DetailView para ver información del usuario
class usuario_detalle(DetailView):
    model: Usuario

# Clase que creara una vista API
class ChartData(APIView):

    # Función que suma los totales de cada pedido en un día para obtener el total diario
    def total_dia(self, dia):
        hoy = date.today()
        dia = hoy - timedelta(days=hoy.weekday()-dia)
        total_dia = 0
        for pedido in Pedido.objects.filter(fecha=dia):
            total_dia += pedido._total()
        return total_dia

    def get(self, request, format=None):
        default_items = [
            self.total_dia(0), # Lunes
            self.total_dia(1), # Martes
            self.total_dia(2), # Miercoles
            self.total_dia(3), # Jueves
            self.total_dia(4), # Viernes
            self.total_dia(5), # Sabado
            self.total_dia(6), # Domingo
            ]
        data = {
            "default": default_items,
        }
        return Response(data)

# Función que realiza los filtros tomando como referencia un request GET
def filtro(request):
    qs = Producto.objects.all()
    restaurante = request.GET.get('restaurante')

    if restaurante != '' and restaurante is not None and restaurante != 'Restaurante':
        qs = qs.filter(restaurante__nombre=restaurante)

    return qs

def productos(request):
    qs = filtro(request)
    context = {
        'productos': qs,
        'restaurantes': Restaurante.objects.all(),
    }
    return render(request, 'reportes/productos.html', context)

def index(request):
    pedidos = list(Pedido.objects.all().order_by('-id'))
    pedidos_totales = Pedido.objects.all().count()
    usuarios_totales = Usuario.objects.all().count()
    repartidores_totales = Repartidor.objects.all().count()
    context = {'pedidos': pedidos, 'pedidos_totales': pedidos_totales,
    'usuarios_totales': usuarios_totales, 'repartidores_totales': repartidores_totales}
    return render(request, 'reportes/index.html', context)

def clientes(request):
    usuarios = list(Usuario.objects.all())
    context = {'usuarios': usuarios}
    return render(request, 'reportes/clientes.html', context)

def reclamos(request):
    reclamos = list(Reclamo.objects.all())
    context = {'reclamos': reclamos}
    return render(request, 'reportes/reclamos.html', context)

def repartidores(request):
    repartidores = list(Repartidor.objects.all())
    context = {'repartidores': repartidores}
    return render(request, 'reportes/repartidores.html', context)

def exportar_pedidos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pedidos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Fecha', 'Cliente', 'Restaurante', 'Productos', 'Estado'])

    pedidos = Pedido.objects.all().values_list('fecha', 'usuario', 'restaurante', 'producto', 'estado')
    for pedido in pedidos:
        writer.writerow(pedido)

    return response
