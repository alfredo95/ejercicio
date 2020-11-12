from django.db import models
from django.forms import ModelForm, ModelChoiceField
from directorio.models import Tienda

# Modelo producto
class Producto(models.Model):
	codigo = models.CharField(max_length = 12, primary_key = True, default = '')
	nombre = models.CharField(max_length = 30, default='', unique = True)
	descripcion = models.CharField(max_length = 100, default='')
	precio = models.DecimalField(max_digits=6, decimal_places = 2, default=0.00)

	def __str__(self):
		return self.nombre


# Modelo tienda
class Inventario(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default = 0)

	class Meta:
		unique_together = ('tienda', 'producto')


# Form producto
class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'

# Form tienda
class InventarioForm(ModelForm):
	class Meta:
		model = Inventario
		producto = ModelChoiceField(queryset = Producto.objects.all())
		fields = ['producto', 'tienda']
