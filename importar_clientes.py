import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prestamos_app.settings')
django.setup()

from clientes.models import Cliente
from decimal import Decimal, InvalidOperation

# Leer archivo
df = pd.read_excel('Prueba1.xlsx')

def limpiar_decimal(valor):
    try:
        if pd.isna(valor):
            return None
        valor = str(valor).replace('$', '').replace(',', '').strip()
        return Decimal(valor)
    except (InvalidOperation, ValueError):
        return None

# Recorrer filas
for i, fila in df.iterrows():
    try:
        Cliente.objects.create(
            nombre=fila['nombre'],      # verifica nombre exacto
            grupo=fila['grupo'],
            capital=limpiar_decimal(fila['capital']),  # CORREGIDO
            interes=int(fila['interes'])
        )
    except Exception as e:
        print(f"Error en fila {i}: {fila}")
        print(e)

print("Clientes importados correctamente")

# Comando: python importar_clientes.py