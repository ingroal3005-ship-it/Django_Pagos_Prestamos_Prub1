from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('cliente/<int:id>/', views.detalle_cliente, name='detalle_cliente'),
]

