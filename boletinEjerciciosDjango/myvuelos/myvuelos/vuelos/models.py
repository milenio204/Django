import datetime

from django.db import models

# Create your models here.


class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    siglas = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre;


class Vuelo(models.Model):
    aeropuerto = models.OneToOneField(Aeropuerto, on_delete=models.CASCADE, primary_key=True)
    aeropuerto_salida = models.DateField(blank=True)
    fecha_salida = models.DateTimeField(blank=True)
    aeropuerto_llegada = models.DateField(blank=True)
    fecha_llegada = models.DateTimeField(blank=True)
    codigo_vuelo = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return self.codigo_vuelo;


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre;


class Reserva(models.Model):
    vuelo = Vuelo
    cliente = Cliente
    fecha_reserva = models.DateTimeField()
    precio = models.FloatField()