from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    capital_inicial = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Porcentajes de rendimiento
    porc_total = models.DecimalField(max_digits=5, decimal_places=2, default=9.00) # 9%
    porc_trabajador = models.DecimalField(max_digits=5, decimal_places=2, default=2.00)
    porc_ganancia = models.DecimalField(max_digits=5, decimal_places=2, default=2.00)
    porc_gastos_sueldos = models.DecimalField(max_digits=5, decimal_places=2, default=2.00)
    porc_reinversion = models.DecimalField(max_digits=5, decimal_places=2, default=3.00)
    
    # Resúmenes actuales
    total_semanal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    pagos_concluidos = models.IntegerField(default=0)
    pagos_atrasados = models.IntegerField(default=0)
    
    # Documentos
    expediente = models.FileField(upload_to='expedientes/', blank=True, null=True)

    def calcular_multa_diaria(self):
        """
            Calcula la multa basada en: $15 por cada $1000 de capital.
        """
        if self.capital_inicial >= 1000:
            # Dividimos el capital entre 1000 y multiplicamos por 15
            unidades_de_mil = self.capital_inicial // 1000
            total_multa = unidades_de_mil * Decimal('15.00')
            return total_multa
        return Decimal('0.00')

    @property
    def multa_sugerida(self):
        return self.calcular_multa_diaria()

class RegistroFinanciero(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='registros')
    fecha = models.DateField(auto_now_add=True)
    monto_pago = models.DecimalField(max_digits=12, decimal_places=2)
    es_abono_capital = models.BooleanField(default=False)
    es_pago_inconcluso = models.BooleanField(default=False)
    comprobante = models.FileField(upload_to='pagos/', blank=True, null=True)

class Multa(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    motivo = models.TextField(default="Mora de $15 por cada $1000")
    fecha = models.DateField(auto_now_add=True)
    pagada = models.BooleanField(default=False)

    def __str__(self):
        return f"Multa de {self.monto} - {self.cliente.nombre}"