from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from catalogo.models import Producto

# Create your views here.

def index(request):
	productos = Producto.objects.order_by('nombre')[:5]
	template = loader.get_template('catalogo/index.html')
	context = {

		'productos': productos,

	}
	return HttpResponse(template.render(context, request))


def borrarProducto(request, id):
	producto = Producto.objects.get(pk=id)
	if(producto is not None):
		producto.delete()
	return redirect('index')