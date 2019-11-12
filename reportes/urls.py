from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('repartidores/', views.repartidores, name='repartidores'),
]