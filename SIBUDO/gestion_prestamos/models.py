from django.db import models

# Create your models here.
class Prestamo(models.Model):
    # Atributos de modelo
    id_est = models.PositiveBigIntegerField()
    tipo_recurso = models.IntegerField()
    id_recurso = models.IntegerField()
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    estado_prestamo = models.IntegerField()

    # Atributos de creacion y modificacion
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
    
    def __str__(self):
        return self.id

class Recurso_Disponible(models.Model):
    # Atributos de modelo
    id_recurso = models.IntegerField()
    tipo_recurso = models.IntegerField()
    n_disponibles = models.PositiveBigIntegerField()
    tipo_prestamo = models.BooleanField()

    # Atributos de creacion y modificacion
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'Recurso_Disponible'
        verbose_name_plural = 'Recursos_Disponibles'

    def __str__(self):
        return self.n_disponibles