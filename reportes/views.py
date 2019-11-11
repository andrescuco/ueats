from django.shortcuts import render

from .models import Pedido

def index(request):
    pedidos = list(Pedido.objects.all())
    context = {'pedidos': pedidos}
    return render(request, 'reportes/index.html', context)
