from django.db import models
from django.forms import ModelForm

# Modelo Tienda
class Tienda(models.Model):
  nombre = models.CharField(max_length = 30, unique = True)
  direccion = models.CharField(max_length = 100)
  telefono = models.IntegerField()
  encargado = models.CharField(max_length = 30)
  def __str__(self):
  	return self.nombre
 
# Form Tienda
class TiendaForm(ModelForm):
	class Meta:
		model = Tienda
		fields = '__all__'