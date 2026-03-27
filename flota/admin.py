from django.contrib import admin
from .models import Sede, Chofer, Camion, Viaje

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'provincia')
    list_filter = ('provincia',)
    search_fields = ('nombre', 'ciudad')

@admin.register(Chofer)
class ChoferAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'estado', 'fecha_ingreso')
    list_filter = ('estado',)
    search_fields = ('apellido', 'nombre')

@admin.register(Camion)
class CamionAdmin(admin.ModelAdmin):
    list_display = ('patente', 'modelo', 'año', 'estado', 'chofer_asignado')
    list_filter = ('estado', 'modelo')
    search_fields = ('patente', 'modelo')

@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('id', 'origen', 'destino', 'fecha', 'estado', 'chofer', 'camion_asignado')
    list_filter = ('estado', 'fecha')
    search_fields = ('origen', 'destino', 'carga')
    date_hierarchy = 'fecha'