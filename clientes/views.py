from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def detalle_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})