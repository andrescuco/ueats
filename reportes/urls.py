from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from .models import Usuario
from . import views
from .views import ChartData, usuario_detalle

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('repartidores/', views.repartidores, name='repartidores'),
    path('productos/', views.productos, name='productos'),
    path('reclamos/', views.reclamos, name='reclamos'),
    path('usuario/<int:pk>/', usuario_detalle.as_view(model=Usuario), name='usuario_detalle'),
    url(r'^exportar/pedidos/csv/$', views.exportar_pedidos_csv, name='exportar_pedidos_csv'),
    url(r'^api/chart/data/$', ChartData.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)