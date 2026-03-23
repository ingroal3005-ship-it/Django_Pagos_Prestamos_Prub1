from django.contrib import admin
from .models import Cliente, RegistroFinanciero, Multa

from django.contrib import admin

admin.site.site_header = "Sistema de Préstamos"
admin.site.site_title = "Panel Administrativo"
admin.site.index_title = "Administración del Sistema"

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Usamos los nombres de campos que definimos para tu Excel
    list_display = ('nombre', 'capital_inicial', 'total_semanal', 'multa_sugerida')
    readonly_fields = ('multa_sugerida',)
    search_fields = ('nombre',)

@admin.register(RegistroFinanciero)
class RegistroFinancieroAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'monto_pago', 'fecha', 'es_abono_capital')
    list_filter = ('es_abono_capital', 'fecha')

@admin.register(Multa)
class MultaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'monto', 'fecha', 'pagada')

