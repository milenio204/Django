import datetime

from django.db import models

# Create your models here.


class Residente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre;


class Familiar(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    parentesco = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre;


class Informe(models.Model):
    nombre_informe : models.CharField(max_length=200)
    fecha_informe = models.DateField()

    def __str__(self):
        return self.nombre_informe;


class ParteInforme(models.Model):
    tipo = ['SANITARIA', 'FUNCIONAL', 'PSIQUICA', 'SOCIAL', 'TERAPIA OCUPACIONAL']
    valoracion_inicial = models.CharField(max_length=200)
    objetivos = models.CharField(max_length=200)
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo;
