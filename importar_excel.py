import pandas as pd
import os
import django

# Estas líneas son necesarias si corres el script por fuera de la consola de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_pagos.settings') # Cambia 'prestamos_project' por el nombre de tu carpeta de configuración
django.setup()

from clientes.models import Cliente

def importar_desde_excel(ruta_archivo):
    # Usamos r'' para evitar errores de ruta en Windows
    df = pd.read_excel(ruta_archivo)
    
    for index, fila in df.iterrows():
        # Usamos update_or_create para evitar duplicar clientes si corres el script dos veces
        Cliente.objects.update_or_create(
            nombre=fila['NOMBRE'],
            defaults={
                'capital_inicial': fila['CAPITAL'],
                'total_semanal': fila['TOTAL SEMANAL'],
                'pagos_atrasados': fila['PAGO INCONCLUSO ATRASADO'] if not pd.isna(fila['PAGO INCONCLUSO ATRASADO']) else 0,
                'pagos_concluidos': fila['PAGOS CONCLUIDOS'] if not pd.isna(fila['PAGOS CONCLUIDOS']) else 0,
                # Agrega los demás porcentajes aquí:
                'porc_total': 9,
                'porc_trabajador': 2,
            }
        )
    print("¡Datos cargados o actualizados con éxito!")

# Para ejecutarlo:
if __name__ == "__main__":
    ruta = r"C:\Users\Luis Antonio ROAL\Proyecto_Prestamos\Prestamos.xlsx"
    importar_desde_excel(ruta)