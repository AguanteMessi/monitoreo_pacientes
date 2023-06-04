from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Estado_pago(models.Model): 
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado

class Paciente_clin(models.Model): 
    nombre = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    tele = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado_pago, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
    