from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    categoria_padre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre;


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    url_imagen = models.CharField(max_length=200)
    precio_unidad = models.FloatField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.nombre;
