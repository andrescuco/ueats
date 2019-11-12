from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('repartidores/', views.repartidores, name='repartidores'),
    path('productos/', views.productos, name='productos'),
    url(r'^exportar/pedidos/csv/$', views.exportar_pedidos_csv, name='exportar_pedidos_csv'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

