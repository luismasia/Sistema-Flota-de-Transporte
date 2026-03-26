from django.contrib import admin
from .models import Sede, Empresa, Chofer, Camion, Viaje

admin.site.register(Sede)
admin.site.register(Empresa)
admin.site.register(Chofer)
admin.site.register(Camion)
admin.site.register(Viaje)