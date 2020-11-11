from django.db import models

# Create your models here.
class Tienda(models.Model):
  nombre = models.CharField(max_length = 30, unique = True)
  direccion = models.CharField(max_length = 100)
  telefono = models.IntegerField()
  encargado = models.CharField(max_length = 30)