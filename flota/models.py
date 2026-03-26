from django.db import models

class Sede(models.Model):
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, related_name='sedes')

    def __str__(self):
        return f"{self.ciudad}, {self.provincia}"

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    año_fundacion = models.IntegerField()
    sede_central = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Chofer(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')

class Camion(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    kilometraje = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')
    chofer_asignado = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True, related_name='camion')

class Viaje(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_curso', 'En curso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]   
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    kilometros = models.IntegerField()
    fecha = models.DateField()
    chofer = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True, related_name='viaje')
    camion_asignado = models.ForeignKey(Camion, on_delete=models.SET_NULL, null=True, related_name='viaje')
    carga = models.CharField(max_length=100)
    estado = models.CharField(max_length=30, choices=ESTADOS, default='activo')



