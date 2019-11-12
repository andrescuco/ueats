from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('repartidores/', views.repartidores, name='repartidores'),
    url(r'^exportar/pedidos/csv/$', views.exportar_pedidos_csv, name='exportar_pedidos_csv'),
]