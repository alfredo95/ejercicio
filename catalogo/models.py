from django.db import models
from directorio.models import Tienda

# Create your models here.
class Producto(models.Model):
	codigo = models.CharField(max_length = 12, primary_key = True, default = '')
	nombre = models.CharField(max_length = 30, default='')
	descripcion = models.CharField(max_length = 100, default='')
	precio = models.DecimalField(max_digits=6, decimal_places = 2, default=0.00)



class Inventario(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default = 0)




