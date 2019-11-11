from django.shortcuts import render

from .models import Pedido
from .models import Usuario

def index(request):
    pedidos = list(Pedido.objects.all())
    context = {'pedidos': pedidos}
    return render(request, 'reportes/index.html', context)

def clientes(request):
    usuarios = list(Usuario.objects.all())
    context = {'usuarios': usuarios}
    return render(request, 'reportes/clientes.html', context)
